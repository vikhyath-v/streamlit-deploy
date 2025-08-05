import streamlit as st

st.set_page_config(page_title="Python Cheatsheet", layout="wide")

st.title("🧠 Python Cheatsheet")

tab1, tab2, tab3 = st.tabs(["🔍 Regex", "🪟 Tkinter Widgets", "🌐 Streamlit Widgets"])

# ------------------- REGEX -----------------------
with tab1:
    st.header("🔍 Regular Expressions (Regex)")

    with st.expander("1️⃣ Basic Syntax Overview"):
        st.markdown("""
        | Pattern | Description | Example |
        |---------|-------------|---------|
        | `.`     | Any character except newline | `a.b` → matches `acb`, `a1b` |
        | `^`     | Start of string | `^Hello` |
        | `$`     | End of string | `end$` |
        | `*`     | 0 or more | `a*` → matches `a`, `aa`, ... |
        | `+`     | 1 or more | `a+` |
        | `?`     | 0 or 1 | `a?` |
        | `{n}`   | Exactly n times | `a{3}` |
        | `{n,}`  | n or more times | `a{2,}` |
        | `{n,m}` | Between n and m times | `a{2,4}` |
        | `[]`    | One of set | `[aeiou]` |
        | `[^]`   | Not in set | `[^0-9]` |
        | `\d`   | Digit | `\d` |
        | `\D`   | Non-digit | `\D` |
        | `\w`   | Word character | `\w` |
        | `\W`   | Non-word | `\W` |
        | `\s`   | Whitespace | `\s` |
        | `\S`   | Non-whitespace | `\S` |
        | `()`    | Grouping | `(abc)+` |
        """)

    with st.expander("2️⃣ Common Use Cases"):
        st.markdown("""
        | Task | Regex Pattern |
        |------|----------------|
        | Validate email | `r'^[\w\.-]+@[\w\.-]+\.\w+$'` |
        | Validate phone number (10 digits) | `r'^\d{10}$'` |
        | Extract all numbers | `r'\d+'` |
        | Extract all words | `r'\w+'` |
        | Only letters | `r'^[A-Za-z]+$'` |
        | Alphanumeric | `r'^[A-Za-z0-9]+$'` |
        | Remove special characters | `re.sub(r'[^A-Za-z0-9 ]+', '', string)` |
        | Match date (dd/mm/yyyy) | `r'\b\d{2}/\d{2}/\d{4}\b'` |
        | Match time (hh:mm) | `r'\b\d{2}:\d{2}\b'` |
        """)

    with st.expander("3️⃣ Regex Flags"):
        st.markdown("""
        | Flag | Use | Example |
        |------|-----|---------|
        | `re.IGNORECASE` / `re.I` | Case-insensitive | `re.search(r'hello', 'HELLO', re.I)` |
        | `re.MULTILINE` / `re.M` | `^`/`$` match lines | |
        | `re.DOTALL` / `re.S` | `.` matches newline too | |
        """)

# ------------------- TKINTER -----------------------
with tab2:
    st.header("🪟 Tkinter Widgets Reference")

    with st.expander("Widget List & Syntax"):
        st.markdown("""
        | Widget | Description | Example |
        |--------|-------------|---------|
        | `Tk()` | Main window | `root = tk.Tk()` |
        | `Label` | Text/image | `tk.Label(root, text="Hello")` |
        | `Button` | Clickable | `tk.Button(root, text="Click", command=cb)` |
        | `Entry` | Single-line input | `tk.Entry(root)` |
        | `Text` | Multi-line text | `tk.Text(root)` |
        | `Spinbox` | Numeric range | `tk.Spinbox(root, from_=0, to=10)` |
        | `Listbox` | List of items | `tk.Listbox(root)` |
        | `Checkbutton` | Checkbox | `tk.Checkbutton(root)` |
        | `Radiobutton` | Radio option | `tk.Radiobutton(root)` |
        | `Scale` | Slider | `tk.Scale(root, from_=0, to=100)` |
        | `Message` | Long text | `tk.Message(root, text="...")` |
        | `Menu` | Menu bar | `tk.Menu(root)` |
        | `Frame` | Container | `tk.Frame(root)` |
        | `Canvas` | Shapes/images | `tk.Canvas(root)` |
        | `Toplevel` | Pop-up | `tk.Toplevel(root)` |
        | `Scrollbar` | Scrollbar | `tk.Scrollbar(root)` |
        | `Combobox` | Dropdown (ttk) | `ttk.Combobox(root)` |
        | `Notebook` | Tabs (ttk) | `ttk.Notebook(root)` |
        | `Progressbar` | Progress bar | `ttk.Progressbar(...)` |
        """)

# ------------------- STREAMLIT -----------------------
with tab3:
    st.header("🌐 Streamlit Widgets Reference")

    with st.expander("📥 Input Widgets"):
        st.markdown("""
        | Widget | Syntax | Purpose |
        |--------|--------|---------|
        | Text Input | `st.text_input("Label")` | Short text |
        | Text Area | `st.text_area("Label")` | Long text |
        | Number Input | `st.number_input("Label", 0, 100)` | Numbers |
        | Date Input | `st.date_input("Select date")` | Select date |
        | Time Input | `st.time_input("Select time")` | Select time |
        | File Upload | `st.file_uploader("Upload")` | Upload file |
        | Color Picker | `st.color_picker("Pick a color")` | Pick color |
        | Slider | `st.slider("Select", 0, 100)` | Select value |
        | Selectbox | `st.selectbox("Choose", options)` | Dropdown |
        | Multiselect | `st.multiselect("Choose", options)` | Multi-option |
        | Radio | `st.radio("Pick one", options)` | Single option |
        | Checkbox | `st.checkbox("I agree")` | On/Off |
        | Password | `st.text_input("Password", type="password")` | Masked text |
        """)

    with st.expander("🖥️ Display Widgets"):
        st.markdown("""
        | Widget | Syntax | Purpose |
        |--------|--------|---------|
        | Write | `st.write("Text")` | Mixed content |
        | Markdown | `st.markdown("**Bold**")` | Rich formatting |
        | Title | `st.title("Title")` | Page title |
        | Header | `st.header("Header")` | Header text |
        | Code | `st.code("code")` | Code block |
        | LaTeX | `st.latex("math")` | Math formula |
        | Metric | `st.metric("Label", "Value")` | KPI metric |
        | Image | `st.image("image.png")` | Display image |
        | Video | `st.video("video.mp4")` | Play video |
        | Audio | `st.audio("audio.mp3")` | Play audio |
        """)

    with st.expander("🧩 Layout & Control Widgets"):
        st.markdown("""
        | Widget | Syntax | Purpose |
        |--------|--------|---------|
        | Columns | `col1, col2 = st.columns(2)` | Side-by-side layout |
        | Tabs | `tab1, tab2 = st.tabs(["A", "B"])` | Tabbed layout |
        | Expander | `with st.expander("Title"):` | Expand/collapse |
        | Sidebar | `st.sidebar.selectbox(...)` | Sidebar UI |
        | Form | `with st.form("form1"):` | Group inputs |
        | Container | `with st.container():` | Widget grouping |
        """)