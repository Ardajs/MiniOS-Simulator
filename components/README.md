#  Components

The `components` package contains reusable user interface components and shared styling utilities used throughout the MiniOS Simulator.

Instead of duplicating interface code across different pages, common UI elements are centralized in this folder, making the project easier to maintain, extend, and customize.

---

##  Folder Structure

```
components/
├── styles.py     # Global Streamlit styles
└── ui.py         # Reusable UI components
```

---

#  Modules

##  styles.py

Defines the global visual theme of the application using custom CSS injected into Streamlit.

### Responsibilities

- Global application styling
- Background colors
- Typography
- Card layouts
- Metric box styling
- Container spacing
- Responsive appearance

### Styled Elements

- Application background
- Main titles
- Subtitles
- Section cards
- Information panels
- Feature lists
- Metric components
- Layout spacing

This module ensures that every page has a consistent and professional appearance.

---

##  ui.py

Contains reusable UI components that simplify page development and improve consistency across the application.

### Components

### `page_header()`

Creates a standardized page header.

Features:

- Large page title
- Subtitle/description
- Consistent page layout

---

### `section_card()`

Displays information inside a reusable card component.

Features:

- Section title
- Description text
- Modern card layout

---

### `info_card()`

Displays lists of features or module information.

Features:

- Card title
- Bullet list
- Reusable information layout

---

#  Design Goals

The Components package follows several software engineering principles:

- **Reusability** – Common UI elements are written once and reused throughout the project.
- **Consistency** – Every page shares the same design language and layout.
- **Maintainability** – UI updates only need to be made in one place.
- **Modularity** – Components are independent and easy to extend.
- **Scalability** – New pages can easily reuse existing components.

---

# Usage
Each page imports the required components instead of implementing them repeatedly.

Example:

```python
from components.styles import load_styles
from components.ui import page_header, section_card, info_card
```

This approach keeps the project clean, organized, and aligned with modern software architecture practices.

---

#  Purpose

The Components package serves as the shared presentation layer of the MiniOS Simulator.

By separating styling and reusable UI elements from business logic, the project becomes easier to develop, maintain, and expand as new operating system modules are added.
