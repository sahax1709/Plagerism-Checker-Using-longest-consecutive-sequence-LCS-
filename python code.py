import tkinter as tk
from tkinter import ttk
import time

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a table to store lengths of longest common subsequences
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Build lcs_table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Length of longest common subsequence is at lcs_table[m][n]
    return lcs_table[m][n]

def calculate_similarity():
    text1 = text_box1.get("1.0", "end-1c")
    text2 = text_box2.get("1.0", "end-1c")

    # Calculate the length of the longest common subsequence
    lcs_length = longest_common_subsequence(text1, text2)

    # Calculate the similarity ratio
    similarity_ratio = (lcs_length / max(len(text1), len(text2))) * 100

    # Create loading bar
    progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
    progress_bar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Update progress bar
    for i in range(int(similarity_ratio)):
        time.sleep(0.03)  # Simulate loading
        progress_bar["value"] = i
        root.update_idletasks()

    # Show similarity result on screen
    result_label.config(text=f"Similarity: {similarity_ratio:.2f}%", fg="#00203F")

    # Show likelihood of plagiarism
    if similarity_ratio >= 50:
        plagiarism_label.config(text="Most likely plagiarism detected.", fg="#FF5733")
    else:
        plagiarism_label.config(text="No plagiarism detected.", fg="#228B22")

# Create the main window
root = tk.Tk()
root.title("Plagiarism Checker")

# Set window size
window_width = 1000
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

# Set background color
root.configure(bg="#F3E5F5")

# Set font
font_style = ("Arial", 12)

# Create text input boxes
text_box1_label = tk.Label(root, text="Enter Paragraph 1:", bg="#CE93D8", fg="#FFFFFF", font=font_style)
text_box1_label.place(relx=0.1, rely=0.3, anchor=tk.CENTER)
text_box1 = tk.Text(root, height=8, width=80)
text_box1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

text_box2_label = tk.Label(root, text="Enter Paragraph 2:", bg="#CE93D8", fg="#FFFFFF", font=font_style)
text_box2_label.place(relx=0.1, rely=0.5, anchor=tk.CENTER)
text_box2 = tk.Text(root, height=8, width=80)
text_box2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create button to calculate similarity
calculate_button = tk.Button(root, text="Check Plagiarism", command=calculate_similarity, bg="#7E57C2", fg="white", font=font_style)
calculate_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Create label to display similarity result
result_label = tk.Label(root, text="", bg="#F3E5F5", font=("Arial", 16))
result_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# Create label to indicate likelihood of plagiarism
plagiarism_label = tk.Label(root, text="", bg="#F3E5F5", font=("Arial", 12))
plagiarism_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Run the Tkinter event loop
root.mainloop()
