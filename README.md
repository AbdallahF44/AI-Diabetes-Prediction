# AI Diabetes Prediction 🤖🍬

**Project Description**  
This project utilizes Artificial Intelligence to predict the likelihood of developing diabetes at an early stage based on organized medical data such as glucose levels, blood pressure, BMI, age, and more. The goal is to support medical decision-making and improve early detection.

---

## 🛠️ Technologies Used

- **Python**  
- Libraries: `scikit-learn` for model building, `pandas`, `numpy`, `matplotlib`/`seaborn` for visualization  
- Techniques: SVM, Random Forest, and SMOTE for handling imbalanced data  
- Model optimization using `GridSearchCV`

---

## ⚙️ Project Structure

AI-Diabetes-Prediction/
├── data/ # PIMA dataset or CSV files
├── notebooks/ # Exploratory analysis and model training
├── src/ # Data processing and model training scripts
├── results/ # Plots and confusion matrices
├── requirements.txt # Project dependencies
└── README.md



## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/AbdallahF44/AI-Diabetes-Prediction.git
cd AI-Diabetes-Prediction
```
2. Create a virtual environment and install the dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```
3. Run training and prediction:

- **Open Jupyter Notebook inside the notebooks/ folder for interactive testing.**
- **Or run scripts directly from src/:**

```bash
python src/train_model.py
python src/predict.py --input data/sample.csv
```
## 📊 Results and Evaluation
- **Performance comparison between SVM and Random Forest**
- **Used SMOTE to balance the dataset**
- **Evaluation metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix**
- **Visualized results using charts and plots**

## 📝 Contributions
Contributions are always welcome! Please feel free to open an issue or submit a pull request for improvements.

## 📄 License
This project is licensed under the MIT License.

## ✉️ Contact Information
- **GitHub: @AbdallahF44**
- **Email: abdallahfawziabumostafa@gmail.com**

