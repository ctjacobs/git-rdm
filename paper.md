---
title: 'Git-RDM: A research data management plugin for the Git version control system'
tags:
  - Git
  - Research Data Management
  - plugin
  - version control
  - figshare
  - Zenodo
  - digital curation
  - Digital Object Identifiers
authors:
 - name: Christian T. Jacobs
   orcid: 0000-0002-0034-4650
   affiliation: University of Southampton
 - name: Alexandros Avdis
   orcid: 0000-0002-2695-3358
   affiliation: Imperial College London
date: 16 June 2016
bibliography: paper.bib
---

# Summary

Many research funding agencies [@RCUK_2015] and research societies [@RS_2012] are increasingly requiring that data from at least publicly funded research be made openly available, and with clear citations that describe provenance. These requirements have led to the proliferation of institutional repositories with universities maintaining a handful of data services, but also repository services capable of minting a persistent and citable Digital Object Identifier (DOI) [@ISO26324_2012] for every published item. Figshare (figshare.com) and Zenodo (zenodo.org) are examples of the latter. Alongside data, software is also increasingly seen as a research output. This viewpoint necessitates not just open-source publication of code, but also provenance and attribution. While a DOI is an identifier of static items, many research teams use version control systems and services to organise their collective efforts and publish output, be that code or data. Popular examples include Git [@ChaconStraub_2014] and GitHub (github.com).

Git-RDM is a Research Data Management (RDM) plugin for the Git version control system. It interfaces Git with data hosting services to manage the curation of version controlled files using persistent, citable repositories. This facilitates the sharing of research outputs and encourages a more open workflow within the research community.

Much like the standard Git commands, Git-RDM allows users to add/remove files within a 'publication staging area'. When ready, users can readily publish these staged files to a data repository hosted either by Figshare or Zenodo via the command line; this curation step is handled by the PyRDM library [@Jacobs_etal_2014]. Details of the files and their associated publication(s) are then recorded in a local SQLite database, including the specific Git revision (in the form of a SHA-1 hash), publication date/time, and the DOI, such that a full history of data publication is maintained.

# References
