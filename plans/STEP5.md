# Update Alongside

We want to work on an updated version of the Alongside (https://www.alongsidens.ca/) website, that exists separate from the existing website (for now, to be hosted in a subdirectory). The current site is built with static HTML from a WYSIWYG tool; this update will involve extracting the text content and migrating it to a static-site generator (Pelican).

The updated site will have the following changes:

 - **Migration to Pelican**: Extract text content from the existing HTML and wrap it into a new Pelican static-site structure.
 - **"Working with us" page**: Provide specific instructions telling people what to do if they want to work with Alongside. (This will include reminding them to provide a phone number. Placeholder text will be used for now.)
 - **Hiring Needs Banner**: Every page except "working with us" will have a box near the top that links to "working with us", and provides a short description of current hiring needs. If there are no current hiring needs, this box disappears. (This will be managed via static Pelican configuration/templates for now.)
 - **Contact page**: This page will be removed.
 - **Global Footer**: Contact information will be added to a banner along the bottom of every page, with Sommerset listed as the main office. (Placeholder contact details will be used initially.)
 - **FAQs Page**: A new page of “FAQs/Frequently Asked Questions” will be added, and we expect to change the questions several times as we figure out what will be useful there. (Placeholder Q&As will be used initially.)
