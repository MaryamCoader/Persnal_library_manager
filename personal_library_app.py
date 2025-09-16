# personal_library_app.py
# A simple personal library management app using Streamlit

import streamlit as st
import json
import os

FILE_NAME = "library.json"

# Load books from JSON file
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save books to JSON file
def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

# App title
st.set_page_config(page_title="📚 Personal Library Manager", layout="centered")
st.title("📚 Personal Library Manager")

# Load current books
books = load_books()

# Sidebar for navigation
menu = st.sidebar.radio("Menu", ["Add Book", "View Books", "Search Book", "Delete Book"])

# 1. Add Book
if menu == "Add Book":
    st.subheader("➕ Add a New Book")
    with st.form("add_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.text_input("Publication Year")
        submitted = st.form_submit_button("Add Book")
        
        if submitted:
            if title and author and year:
                books.append({"title": title, "author": author, "year": year})
                save_books(books)
                st.success(f"✅ Book '{title}' added!")
            else:
                st.error("⚠️ Please fill all fields.")

# 2. View Books
elif menu == "View Books":
    st.subheader("📖 All Books in Your Library")
    if books:
        for i, book in enumerate(books, 1):
            st.write(f"**{i}.** {book['title']} by {book['author']} ({book['year']})")
    else:
        st.info("No books found. Add some!")

# 3. Search Book
elif menu == "Search Book":
    st.subheader("🔍 Search Book")
    keyword = st.text_input("Enter title or author name")
    if keyword:
        results = [b for b in books if keyword.lower() in b['title'].lower() or keyword.lower() in b['author'].lower()]
        if results:
            st.write("### Results:")
            for book in results:
                st.write(f"- {book['title']} by {book['author']} ({book['year']})")
        else:
            st.warning("No matching book found.")

# 4. Delete Book
elif menu == "Delete Book":
    st.subheader("❌ Delete a Book")
    if books:
        options = [f"{b['title']} by {b['author']} ({b['year']})" for b in books]
        book_to_delete = st.selectbox("Select a book to delete", options)
        if st.button("Delete"):
            index = options.index(book_to_delete)
            removed = books.pop(index)
            save_books(books)
            st.success(f"✅ Removed '{removed['title']}' from library.")
    else:
        st.info("No books to delete.")

