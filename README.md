# Markdown Storage

Reads folder structure with markdown files.
Splits meta-data and contents and makes data accessible via chainable API.

Given this folder structure:
    .
    . sample_content
        . projects
            . jobplatform.md


Where jobs.md includes

    title: Jobs
    slug: jobs
    ---
    # Project description

    orem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat.

Access the contents with this snippet:

    > from markdown_storage.folder import ContentFolder
    > root = ContentFolder('./sample_content/')
    > root.projects.jobs.meta
    {'slug': 'jobs', 'title': 'Jobs'}

    > root.projects.contents
    '<h1>Project description</h1>\n<p>orem ipsum dolor sit amet, consectetur
    adipiscing elit,\nsed do eiusmod tempor incididunt ut labore et dolore
    magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco
     laboris nisi\nut aliquip ex ea commodo consequat.</p>'


## SETUP DEVELOPMENT ENVIRONMENT

    $ make develop


## RUN TESTS

    $ make test


## BUILD PYTHON PACKAGE

    $ make build