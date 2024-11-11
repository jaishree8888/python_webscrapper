import requests
from tkinter import *
from tkinter import messagebox
API_KEY = "a1a70ef388ce41a89dbad54cbe7c6e24"
def find():
    topic = entry.get()
    file_name = entry_2.get()
    if not topic:
        messagebox.showerror("Error", "Topic cannot be empty")
        return
    if not file_name:
        messagebox.showerror("Error", "File name cannot be empty")
        return
    if not file_name.endswith(".html"):
        file_name += ".html"
    try:
        url = f'https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get('articles')
        if not articles:
            messagebox.showinfo("Result", "No articles found.")
            return
        # Create an HTML content for the output
        html_output = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Scraped Content</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                h1 {
                    color: #333;
                }
                .article {
                    margin-bottom: 20px;
                }
                .title {
                    font-size: 1.5em;
                    color: #333;
                }
                .description {
                    font-size: 1.2em;
                    color: #555;
                }
                .link {
                    font-size: 1em;
                    color: #1a0dab;
                }
            </style>
        </head>
        <body>
            <h1>News Articles for given Topic</h1>
        """
        for article in articles:
            html_output += f"""
            <div class="article">
                <div class="title">{article['title']}</div>
                <div class="description">{article['description']}</div>
                <div class="link"><a href="{article['url']}">Read more</a></div>
            </div>
            """
        html_output += """
        </body>
        </html>
        """
        # Save the result to an HTML file
        with open(file_name, "w", encoding='utf-8') as file:
            file.write(html_output)
        messagebox.showinfo("Success", f"Content saved to {file_name}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
# Create the main window
root = Tk()
root.title("News Web Scraper")
root.geometry("500x400")
root.resizable(False, False)
# Styling options
font_large = ('arial', 16, 'bold')
font_medium = ('arial', 14)
font_small = ('arial', 12)
# Set background color and style
root.configure(bg="#f0f0f0")
# Create and place widgets
label = Label(root, text="Enter Topic", font=font_large, fg="black", bg="#f0f0f0")
label.place(x=160, y=30)
entry = Entry(root, width=45, font=font_small, bd=2, relief=SOLID)
entry.place(x=50, y=70)
label_2 = Label(root, text="Save file as", font=font_medium, fg="green", bg="#f0f0f0")
label_2.place(x=40, y=130)
entry_2 = Entry(root, font=font_small, bd=2, relief=SOLID)
entry_2.place(x=200, y=130, width=250)
button = Button(root, width=15, text="Scrape and Save", font=font_medium, bg="#4CAF50", fg="white", command=find, bd=2, relief=RAISED)
button.place(x=160, y=200)
# Run the application
root.mainloop()
