# BptImporter

Importer for BrownPaperTickets's (broken) .xlsx Audience Report files.

The ticket vendor BrownPaperTickets allows you to download Audience Reports of your customer data as an Excel file. These are not valid Excel files though, just a tab-separated file with ticket types (Walk-in, Online, etc) organized into sections. This library imports them to a dataframe with labeled ticket types.

Usage demonstrated in `sample.py`. Requires `pandas`.
