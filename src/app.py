import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page configuration
st.set_page_config(page_title="Alzheimer DGE Dashboard", layout="wide")

# Title and description
st.title("🧬 Transcriptomic Analysis: Alzheimer's vs. Control")
st.markdown("""
This application presents the results of Differential Gene Expression (DGE) 
analysis based on RNA-Seq data (GSE203206 dataset). 
Use the sidebar to filter the results dynamically!
""")

# Load data function
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/deseq2_results_annotated.csv', index_col=0)
    return df

try:
    results_df = load_data()
    
    # --- SIDEBAR FOR INTERACTIVE FILTERING ---
    st.sidebar.header("Filter Settings")
    p_val_threshold = st.sidebar.number_input("Adjusted P-value threshold", min_value=0.001, max_value=0.100, value=0.050, step=0.005, format="%.3f")
    lfc_threshold = st.sidebar.number_input("Log2 Fold Change threshold", min_value=0.0, max_value=5.0, value=1.0, step=0.1, format="%.1f")

    # --- DATA PROCESSING FOR PLOT ---
    st.subheader("Interactive Volcano Plot")
    
    df_plot = results_df.dropna(subset=['padj', 'log2FoldChange']).copy()
    df_plot['-log10(padj)'] = -np.log10(df_plot['padj'])
    
    # Dynamic classification based on user input
    df_plot['Significance'] = 'Not significant'
    df_plot.loc[(df_plot['padj'] < p_val_threshold) & (df_plot['log2FoldChange'] > lfc_threshold), 'Significance'] = 'Up-regulated'
    df_plot.loc[(df_plot['padj'] < p_val_threshold) & (df_plot['log2FoldChange'] < -lfc_threshold), 'Significance'] = 'Down-regulated'

    # --- PLOTLY CHART ---
    fig = px.scatter(
        df_plot, 
        x='log2FoldChange', 
        y='-log10(padj)',
        color='Significance',
        color_discrete_map={
            'Up-regulated': 'red', 
            'Down-regulated': 'blue', 
            'Not significant': 'lightgrey'
        },
        hover_name='Gene_Symbol', # Now we use the real biological names!
        hover_data={'log2FoldChange': ':.2f', 'padj': ':.2e', 'Significance': False, '-log10(padj)': False},
        title='Volcano Plot: Alzheimer vs Control',
        labels={'log2FoldChange': 'Log2 Fold Change', '-log10(padj)': '-Log10 Adjusted P-value'}
    )
    
    # Dynamic threshold lines
    fig.add_hline(y=-np.log10(p_val_threshold), line_dash="dash", line_color="black")
    fig.add_vline(x=lfc_threshold, line_dash="dash", line_color="black")
    fig.add_vline(x=-lfc_threshold, line_dash="dash", line_color="black")

    # Display plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

# --- PATHWAY ENRICHMENT PLOT ---
    st.subheader("Top Enriched Biological Processes (Up-regulated Genes)")
    
    try:
        enrichment_df = pd.read_csv('data/processed/enrichment_upregulated.csv')
        
        # Bierzemy top 10 szlaków i odwracamy kolejność, żeby najistotniejszy był na górze wykresu
        top_pathways = enrichment_df.head(10).iloc[::-1]
        
        # Transformujemy P-value dla lepszej czytelności na osi X
        top_pathways['-log10(P-value)'] = -np.log10(top_pathways['P-value'])
        
        # Czyścimy nazwy szlaków (usuwamy kody GO na końcu np. "(GO:0035924)")
        top_pathways['Clean_Term'] = top_pathways['Term'].apply(lambda x: x.split(' (GO:')[0])
        
        fig_pathway = px.bar(
            top_pathways, 
            x='-log10(P-value)', 
            y='Clean_Term',
            orientation='h',
            title='Gene Ontology: Biological Process',
            labels={'Clean_Term': 'Biological Process', '-log10(P-value)': '-Log10 P-value'},
            color='-log10(P-value)',
            color_continuous_scale='Reds'
        )
        
        st.plotly_chart(fig_pathway, use_container_width=True)
        
    except FileNotFoundError:
        st.warning("Pathway enrichment data not found. Run the enrichment notebook first.")

    # --- DATA TABLE ---
    st.subheader("DGE Results Table")
    st.dataframe(results_df)

except FileNotFoundError:
    st.error("Results file not found. Please check your data path.")