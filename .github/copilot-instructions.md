# Project Description

This project is an educational website for sharing homework assignments and coding exercises with students. Students can browse, view, and download assignments directly from the portal.

## Project Structure

- [`assignments/`](../assignments/) Each homework assignment is stored in its own subfolder with a consistent structure.
- [`templates/`](../templates/) Reusable templates for new content
- [`assets/`](../assets/) Contains the website assets including CSS, JavaScript, images, and configuration files
- [`index.html`](../index.html) The main website page that serves as a static portal for browsing and viewing assignments. Content is configurable via [`config.json`](../config.json) file to dynamically generate assignment lists and details.

## Project Guidelines

- Maintain consistent styling across all pages
- Keep file and folder names descriptive and organized

## Educational Standards

When generating content for this project:

- **Learning-focused**: All content should be designed with clear learning objectives and appropriate difficulty levels
- **Student-friendly**: Use clear, encouraging language that motivates students

## Git Guidelines
- Use semantic commit messages to clearly indicate the purpose of each commit. Follow given format strictly: `<type>(<scope>): <description>`  
- Use the following scopes for commit messages:
  - `assignments`: Documentation changes
  - `assets`: Changes to CSS, JavaScript, images, or configuration files
  - `templates`: Changes to reusable templates
  - n/a: General changes that do not fit into the above categories
  - if a new folder is created, use that as a scope in the commit message as well
  - Example commit message: `feat(assignments): Add new assignment on JavaScript basics`
  - Example commit general message: `fix: Correct typos in README.md`