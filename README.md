# IARE-Placement-AGENT
for collge student what skill need for what jobs 

Yes. For your **IARE AI Agent**, you can use the placement posters as the knowledge source and implement **RAG (Retrieval-Augmented Generation)**.

The basic flow should be:

```text
IARE Placement Documents
        ↓
   Extract Text
        ↓
   Split into chunks
        ↓
 Create Embeddings
        ↓
 Vector Database
        ↓
User asks question
        ↓
 Retrieve relevant chunks
        ↓
      LLM
        ↓
 Answer from IARE knowledge
```

## 1. Create `README.md` in your GitHub project

Copy this into a file named **README.md**:

````markdown
# IARE Placement AI Agent

An AI-powered chatbot that answers questions about IARE placement information using
Retrieval-Augmented Generation (RAG).

## 🎯 Purpose

This AI Agent helps IARE students get placement-related information such as:

- Company eligibility
- Required branches
- CGPA requirements
- Backlog requirements
- Salary packages
- Recruitment process
- Job roles
- Required skills
- Placement preparation

The chatbot uses placement documents and recruitment notices as its knowledge base.

---

## 🧠 RAG Architecture

```text
IARE Placement Documents
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Embeddings
        ↓
Vector Database
        ↓
User Question
        ↓
Similarity Search
        ↓
Relevant Information
        ↓
LLM
        ↓
Final Answer
````

## 📚 Current Knowledge

### Accenture

**Role:**

* Associate Software Engineer
* Advanced Associate Software Engineer

**Salary:**

* ₹4.5 - ₹6.5 LPA

**Eligibility:**

* B.Tech
* No Active Backlogs
* CSE
* IT
* CSIT
* CSE (AI & ML)
* CSE (DS)
* CSE (CS)
* ECE
* EEE
* Aero
* MECH
* Civil

**Selection Process:**

1. Cognitive & Technical Ability
2. Coding Assessment
3. Communication Assessment
4. Technical Interview

---

### Tata Technologies

**Hiring:**

* GET / PGET
* 2026 Batch

**Salary:**

* ₹4.5 - ₹5.75 LPA

**Eligibility:**

* 60% or 6.5 CGPA throughout
* No Active Backlogs
* B.Tech - AERO
* M.Tech - AEROSPACE
* One year gap in academics allowed

**Selection Process:**

1. Aptitude Test
2. Technical Interview
3. HR Round

**Useful Skills:**

* C#
* Java
* VBScript
* AA
* UiPath
* BluePrism
* Java/J2EE
* Angular
* RPA
* MPMLink
* Uforia
* ThingWorx
* MS Office
* Excel
* PowerPoint
* SQL
* Charting and Reporting

---

## 🔎 Example Questions

The AI Agent should be able to answer questions such as:

### Example 1

**User:**

> What is the eligibility for Accenture?

**AI:**

> Accenture requires B.Tech students with no active backlogs. Eligible branches include CSE, IT, CSIT, CSE (AI & ML), CSE (DS), CSE (CS), ECE, EEE, Aero, MECH and Civil.

### Example 2

**User:**

> What is the Accenture salary?

**AI:**

> The salary mentioned in the placement notice is ₹4.5 - ₹6.5 LPA.

### Example 3

**User:**

> What is the Tata Technologies selection process?

**AI:**

> The process consists of an Aptitude Test, Technical Interview and HR Round.

### Example 4

**User:**

> Does Tata Technologies require SQL?

**AI:**

> Yes. The placement notice states that knowledge of SQL is an added advantage.

---

## 🛠️ Suggested Technology Stack

* Python
* LangChain
* Sentence Transformers / Embeddings
* FAISS / ChromaDB
* LLM API
* Streamlit
* GitHub

---

## 📁 Project Structure

```text
iare-placement-ai-agent/
│
├── data/
│   ├── placement_documents/
│   └── recruitment_notices/
│
├── embeddings/
│
├── app.py
├── rag.py
├── ingest.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 RAG Implementation

### Step 1: Add Documents

Add IARE placement PDFs, images, notices and other placement information
inside:

```text
data/placement_documents/
```

### Step 2: Extract Text

Extract text from PDFs/images.

### Step 3: Split Text

Split the extracted information into smaller chunks.

Example:

```text
Chunk 1:
Accenture eligibility

Chunk 2:
Accenture recruitment process

Chunk 3:
Tata Technologies eligibility

Chunk 4:
Tata Technologies skills
```

### Step 4: Create Embeddings

Convert each chunk into a vector representation.

### Step 5: Store in Vector Database

Store the embeddings using FAISS or ChromaDB.

### Step 6: Retrieve

When a student asks a question, retrieve the most relevant chunks.

### Step 7: Generate Answer

Send the retrieved information to the LLM and generate an answer.

---

## ⚠️ Important Rule

The AI Agent should answer using the available IARE placement knowledge.

If the information is not available, it should say:

> "I don't have this information in my IARE placement knowledge base."

It should not invent eligibility, salary, company requirements or recruitment dates.

---

## 📌 Disclaimer

Placement information can change. Students should verify the latest official
notification from the IARE Placement and Training Centre before applying.

---

## 👨‍💻 Project

**IARE Placement AI Agent**

Built to help IARE students quickly understand placement opportunities
and eligibility requirements.

````

## 2. How to add `README.md` to GitHub

### If your project is already on GitHub

Go to your repository.

Example:

```text
GitHub
 ↓
Your Repository
 ↓
Add file
 ↓
Create new file
````

For the filename enter:

```text
README.md
```

Paste the README above.

Then:

```text
Commit changes
```

That's it.

---

## 3. Better approach for your RAG

**Don't put all your placement information only inside README.md.**

Use:

```text
README.md
     ↓
Project explanation

data/
     ↓
Actual placement knowledge

RAG
     ↓
Reads data/
     ↓
Creates embeddings
     ↓
Answers students
```

For example:

```text
iare-placement-agent/
│
├── README.md
│
├── data/
│   ├── accenture.txt
│   ├── tata-technologies.txt
│   ├── placement-rules.txt
│   └── company-notices/
│
├── ingest.py
├── rag.py
├── app.py
├── requirements.txt
└── .gitignore
```

**This is the important part:** put the actual information from your IARE posters/PDFs into the `data` folder, and make your RAG system read that folder. README explains the project; **RAG uses the documents as its knowledge base.**

If you want, I can also give you the **complete working Python RAG code (`ingest.py + rag.py + app.py + requirements.txt`)** for this IARE Placement AI Agent.



