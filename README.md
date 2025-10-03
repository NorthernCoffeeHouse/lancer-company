````markdown
# Technical Design Document (TDD)

## Project: Owls Tree Profile Page

---

### 1. Background
- **Style**: Gradient background
- **Definition**:
  ```css
  body {
    background: linear-gradient(135deg, #c8b89a 0%, #d4c4a8 100%);
  }
````

* Provides a warm parchment-like tone to match the theme.

---

### 2. Fonts & Typography

* **Imported Font**:

  ```css
  @font-face {
    font-family: 'Ryzes';
    src: url('frontpage/Ryzes-ax92x.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
  }
  ```
* **System Fallbacks**:
  `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`
* **Usage Rules**:

  * **Username / Headings**:
    `font-family: 'Ryzes', sans-serif; font-size: 24px; font-weight: 600; color: #2c2c2c;`
  * **Body text (bio, footer, link labels)**:
    `font-family: system sans-serif fallback; font-size: 14–16px; color: #4a4a4a;`
  * **Featured card caption**:

    ```css
    .featured-text {
      font-family: 'Comic Sans MS', 'Comic Sans', cursive;
      font-size: 0.8rem;
      letter-spacing: 1px;
      color: #fff;
    }
    ```

---

### 3. Color Palette

| Name             | Hex               | Usage                          |
| ---------------- | ----------------- | ------------------------------ |
| Background Light | `#c8b89a`         | Gradient start                 |
| Background Dark  | `#d4c4a8`         | Gradient end                   |
| Primary Text     | `#2c2c2c`         | Username / Headings            |
| Secondary Text   | `#4a4a4a`         | Bio / supporting text          |
| Link Default     | `#39393A`         | Footer + buttons text          |
| Link Hover       | `#000000`         | Footer + buttons text on hover |
| X Icon           | `#000000`         | Background for X button        |
| LinkedIn Icon    | `#0077b5`         | Background for LinkedIn button |
| GitHub Icon      | `#333333`         | Background for GitHub button   |
| Extra Icon       | `#bb2a2a`         | Background for custom button   |
| Overlay Gradient | `rgba(0,0,0,0.6)` | Featured card image overlay    |

---

### 4. Container (Card Style)

* **Element**: `.container`
* **Purpose**: Main content wrapper for profile and links.
* **Definition**:

  ```css
  .container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 24px;
    padding: 40px 30px;
    width: 90%;
    max-width: 500px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  }
  ```
* **Effect**: Glassmorphism look, rounded corners, centered.

---

### 5. Footer

* **Element**: `.footer`
* **Purpose**: Fixed navigation at bottom of viewport.
* **Definition**:

  ```css
  .footer {
    width: 100%;
    text-align: center;
    padding: 16px 0 8px 0;
    background: rgba(255, 255, 255, 0.2);
    font-size: 16px;
    color: #39393A;
    position: fixed;
    left: 0;
    bottom: 0;
    z-index: 100;
    backdrop-filter: blur(4px);
  }

  .footer a {
    color: #39393A;
    text-decoration: underline;
  }

  .footer a:hover {
    color: #000;
  }
  ```
* **Content**:

  ```html
  <div class="footer">
    <a href="index.html">Go to Homepage</a>
  </div>
  ```

---

### 6. Responsive Design

* **Breakpoint**: `max-width: 480px`
* **Adjustments**:

  * Container padding reduced (`30px 20px`).
  * Link button padding reduced (`12px 16px`).
  * Font size shrinks slightly (14px for buttons).
* Ensures usability on small devices.

---

### 7. Interaction & Motion

* **Profile image**: hover → subtle scale-up (`transform: scale(1.05)`).
* **Buttons**: hover → lighter background + elevation (`transform: translateY(-2px)` + shadow).
* **Featured project card**: hover → slight lift effect.
* **Overall**: fast transitions (`0.2–0.3s ease`) for smooth interactions.

---

### 8. Accessibility

* **Aria labels**: all interactive links and cards include descriptive labels.
* **Contrast**:

  * Dark text over light backgrounds.
  * White text over dark overlays.
* **Navigation**: links open in the **same tab** (`target="_self` or omitted).

---

## Summary

This design achieves:

* **Warm, readable background** with parchment tones.
* **Glassmorphism cards** with soft edges.
* **Custom typography**: Ryzes for headings, system sans-serif for body, casual font for featured text.
* **Consistent footer navigation** at bottom of screen.
* **Accessible, responsive, interactive UI** suitable for desktop and mobile.

```

---

Do you also want me to **add a section with reusable CSS variables** (like `--primary-text`, `--secondary-text`, `--bg-light`) so the TDD doubles as a design system reference?
```
