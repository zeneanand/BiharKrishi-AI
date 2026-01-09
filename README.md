# BiharKrishi-AI
---

# 🌾 BiharKrishi AI: Smart Farming Assistant

**BiharKrishi AI** is a functional, AI-powered web application built to assist marginal farmers in Bihar, India. The application leverages Google's **Gemini 1.5 Pro** model to provide region-specific, actionable, and formatted agricultural advice. It specifically addresses the "Flood-Drought Paradox" and high irrigation costs faced by farmers in the region.

## 📖 Project Overview

* 
**Assignment Title:** Designing a Smart Farming Assistance Web App using Generative AI (FA 2).


* 
**Target Region:** Bihar, India.


* 
**Core Technology:** Python, Streamlit Cloud, and Google Gemini 1.5 API.


* **User Persona:** Ram Kumar Baitha, a marginal farmer from Kishanganj with 0.25 hectares of land.

## 🚀 Features

* 
**Context-Aware Recommendations:** Provides advice based on the user's specific district, crop stage, and farming category.


* 
**Optimized Output Formatting:** Delivers responses in bulleted lists with clear justifications ("the why") for every suggestion to build user trust.


* 
**Simplified Language:** AI outputs are tailored for non-technical audiences using simple, layperson language.


* 
**Global Accessibility:** Deployed via Streamlit Cloud for cross-device testing and use.



## 🛠️ Technical Implementation

### 📂 Files Included

1. 
**`app.py`**: The main Python script containing the Streamlit interface and Gemini 1.5 API integration.


2. 
**`requirements.txt`**: A list of essential Python libraries required to run the application.



### ⚙️ Model Parameters

To ensure factual accuracy and prevent AI hallucinations, the following parameters were utilized:

* **Model:** `gemini-1.5-flash`
* 
**Temperature:** `0.2` (Low temperature for more deterministic, factual responses).


* **Max Output Tokens:** `400` (Balanced for detailed yet concise advice).

## 🧪 Model Validation & Testing

The assistant was tested against five real-world agricultural prompts. Each response was evaluated based on the following **Feedback Checklist**:

* [x] Is the advice specific to the selected Bihar district? 


* [x] Does the output provide valid and logical reasoning? 


* [x] Is the language simple enough for a layperson? 


* [x] Does the model avoid misleading or unsafe advice? 



## 📦 How to Run

1. **Clone the Repository:**
```bash
git clone https://github.com/YourUsername/BiharKrishi-AI.git

```


2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Launch the App:**
```bash
streamlit run app.py

```

