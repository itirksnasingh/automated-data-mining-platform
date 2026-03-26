class DatasetTypeDetector:

    def __init__(self, df):
        self.df = df
        self.columns = [c.lower() for c in df.columns]

    def detect(self):

        # Retail / Transaction dataset
        retail_keywords = ["invoice", "product", "stock", "item", "transaction"]

        if any(word in col for col in self.columns for word in retail_keywords):
            return "Retail Dataset"

        # Student dataset
        student_keywords = ["score", "grade", "math", "reading", "writing"]

        if any(word in col for col in self.columns for word in student_keywords):
            return "Student Dataset"

        # House price dataset
        house_keywords = ["price", "area", "bedroom", "bathroom"]

        if any(word in col for col in self.columns for word in house_keywords):
            return "House Price Dataset"

        # Loan dataset
        loan_keywords = ["loan", "credit", "income", "approval"]

        if any(word in col for col in self.columns for word in loan_keywords):
            return "Loan Dataset"

        return "General Dataset"