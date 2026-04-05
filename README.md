# 🧬 Alzheimer's Disease Transcriptomic Analysis Dashboard

An end-to-end bioinformatics pipeline for **Differential Gene Expression (DGE)** analysis and **Pathway Enrichment**, featuring an interactive web dashboard. 

## 📌 Project Overview
This project investigates the molecular mechanisms of Alzheimer's Disease (AD) using public RNA-Seq data. It transitions from raw transcriptomic counts to biological interpretation, identifying key biomarkers and disrupted cellular processes.

**Data Source:** [NCBI GEO GSE203206](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203206)  
**Sample Size:** Alzheimer's Disease vs. Neurologically Healthy Controls.

## 🚀 Key Features
- **Statistically Rigorous DGE:** Powered by `PyDESeq2` (Python implementation of the industry-standard DESeq2).
- **Biological Annotation:** Automated mapping from Ensembl IDs to Gene Symbols via `MyGene.info`.
- **Functional Analysis:** Pathway enrichment using `GSEApy` connected to **KEGG** and **GO Biological Process** databases.
- **Interactive Visualization:** A dynamic `Streamlit` dashboard with real-time filtering and interactive Plotly charts.

## 🛠️ Tech Stack
- **Language:** Python 3.14+
- **Analysis:** Pandas, NumPy, PyDESeq2, GSEApy
- **Visualization:** Plotly, Streamlit
- **Version Control:** Git

## 📊 Biological Insights
The analysis successfully identified hallmarks of neurodegeneration, including:
- **Unfolded Protein Response:** Detection of cellular stress linked to amyloid-beta proteotoxicity.
- **Vascular Signaling:** Significant enrichment in VEGF-related pathways, supporting the vascular hypothesis of AD.

## ⚙️ How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/bioinfo-cancer-dge-analysis.git](https://github.com/YOUR_USERNAME/bioinfo-cancer-dge-analysis.git)
   cd bioinfo-cancer-dge-analysis
   ```
2. **Setup Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
3. **Launch the Dashboard:**
   ```bash
   streamlit run src/app.py
   ```

## 📂 Project Structure
- `data/`: Raw and processed transcriptomic data (ignored by Git).
- `notebooks/`: Exploratory Data Analysis and Enrichment pipelines.
- `src/`: Source code for the Streamlit application.