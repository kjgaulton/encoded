# EDW/encoded File object sync testing

# python representation of file below, with just EDW-relevant properties
format_app_out = {u'submitted_by': u'someone@gmail.com', u'file_format': u'fastq', u'md5sum': u'aeaea56e89ecb5acceece72f17d75717', u'accession': u'ENCFF001QZP', u'dataset': u'ENCSR000AAA', u'download_path': u'2013/5/9/ENCFF001QZP.txt.gz', u'replicate': 1, u'date_created': u'2013-05-09', u'output_type': u'reads2', u'submitted_file_name': u'../../../../pre-DCC/wgEncodeCshlLongRnaSeq/20130218_promocell_batches1-2_minus_batch1sFASTQ/SID38242_AC1GKKACXX_7_2.txt.gz'}

# full json from admin GET of file from encoded
format_app_in = {
    "status": "CURRENT",
    "submitted_by": {
        "first_name": "Julien",
        "last_name": "Lagarde",
        "uuid": "f5b7857d-208e-4acc-ac4d-4c2520814fe1",
        "title": "Julien Lagarde",
        "submits_for": [
            "/labs/thomas-gingeras/",
            "/labs/roderic-guigo/"
        ],
        "phone1": "+34 933 160 110",
        "fax": "+34 933 969 983",
        "schema_version": "1",
        "email": "someone@gmail.com",
        "lab": "/labs/roderic-guigo/",
        "timezone": "Europe/Madrid",
        "@id": "/users/f5b7857d-208e-4acc-ac4d-4c2520814fe1/",
        "@type": [
            "user",
            "item"
        ],
        "job_title": "Submitter"
    },
    "uuid": "0424d3a2-6bd8-42dc-b5fb-a179e7f910b4",
    "file_format": "fastq",
    "md5sum": "aeaea56e89ecb5acceece72f17d75717",
    "accession": "ENCFF001QZP",
    "schema_version": "1",
    "dataset": "/experiments/ENCSR000AAA/",
    "download_path": "2013/5/9/ENCFF001QZP.txt.gz",
    "replicate": {
        "status": "CURRENT",
        "submitted_by": "/users/0abbd494-b852-433c-b360-93996f679dae/",
        "biological_replicate_number": 1,
        "uuid": "f7934dc2-7107-4ee1-9653-9b052a8a8420",
        "experiment": "/experiments/ENCSR000AAA/",
        "technical_replicate_number": 1,
        "schema_version": "2",
        "platform": {
            "status": "CURRENT",
            "term_name": "Illumina HiSeq 2000",
            "title": "Illumina HiSeq 2000",
            "url": "http://www.illumina.com/documents/products/datasheets/datasheet_hiseq2000.pdf",
            "term_id": "NTR:0000007",
            "encode2_dbxrefs": [
                "Illumina_HiSeq_2000"
            ],
            "schema_version": "1",
            "geo_dbxrefs": [
                "GPL11154",
                "GPL13112"
            ],
            "date_created": "2013-10-02T18:21:55.402397",
            "aliases": [],
            "@id": "/platforms/03a96eaf-75da-44e2-b4f6-e349e8c3655e/",
            "@type": [
                "platform",
                "item"
            ],
            "uuid": "03a96eaf-75da-44e2-b4f6-e349e8c3655e"
        },
        "paired_ended": false,
        "flowcell_details": [
            {
                "machine": "Unknown",
                "lane": "1",
                "flowcell": "AC1GKKACXX_7"
            },
            {
                "machine": "Unknown",
                "lane": "2",
                "flowcell": "AC1GKKACXX_7"
            }
        ],
        "library": {
            "accession": "ENCLB000ZZZ",
            "alternate_accessions": [],
            "aliases": [
                "thomas-gingeras:SID38242"
            ],
            "submitted_by": "/users/0abbd494-b852-433c-b360-93996f679dae/",
            "documents": [
                {
                    "status": "CURRENT",
                    "submitted_by": {
                        "first_name": "Carrie",
                        "last_name": "Davis",
                        "uuid": "0abbd494-b852-433c-b360-93996f679dae",
                        "title": "Carrie Davis",
                        "submits_for": [
                            "/labs/thomas-gingeras/",
                            "/labs/roderic-guigo/"
                        ],
                        "schema_version": "1",
                        "email": "someone@cshl.edu",
                        "lab": "/labs/thomas-gingeras/",
                        "timezone": "US/Eastern",
                        "@id": "/users/0abbd494-b852-433c-b360-93996f679dae/",
                        "@type": [
                            "user",
                            "item"
                        ],
                        "job_title": "Project Manager"
                    },
                    "uuid": "7aa32299-cc11-4f07-bdaa-a55de6f51a99",
                    "aliases": [
                        "ENCODE:HAoSMC_PC_8121902.2P_general_protocol"
                    ],
                    "attachment": {
                        "download": "SID38242.pdf",
                        "href": "@@download/attachment/SID38242.pdf",
                        "type": "application/pdf"
                    },
                    "schema_version": "1",
                    "references": [],
                    "award": {
                        "description": "The goal of this proposal is to comprehensively identify all sequence-based functional elements associated with transcribed sequences including both protein coding and non-protein coding sequences, characterizing gene structures including transcription start sites (TSS) polyadenylation sites and alternative transcripts detected in a representative and diverse panel of human cells and tissues. Based on the empirically determined characteristics of the detected transcripts uncovered in this proposal, a classification system for transcribed protein coding and non-protein coding portions of the human transcriptome will be established. Our aims include first to generate a comprehensive set of subcellular compartment-specific long (>200 nucleotides, nts) and short (<200 nts) polyadenylated (polyA+) and non-polyadenylated (polyA-) RNA samples from each of the cell types studied. These RNA samples will be analyzed using: a) high density tiling arrays (5 nucleotides [nt] interrogation resolution for long and short RNAs), b) sequencing (pyrosequencing [454] and clonal single molecule sequencing for short RNAs [Solexa]), c) sequenced paired-end ditags (PETs) for 5' TSS and 3' termination locations for polyA+ transcripts and d) sequenced cap analysis of gene expression (CAGE) tags for 5' TSS of polyA- RNAs. Characterization of full length subcellular compartment-specific transcripts will also be carried out using: 1) a combination of rapid amplification of cDNA ends (RACE), RT-PCR and sequencing, 2) RNA immunoprecipitation (RIP) and 3) in situ immunohistochemistry. These characterization steps will provide additional information concerning the annotated and unannotated RNAs found to be associated with known functional, compartment-specific proteins and their localization in subcellular organelles of known function. The research and health-care community are well positioned to take advantage of a detailed catalog of classified transcribed regions in the human genome. For example, the identification of millions of single nucleotide polymorphism (SNPs) and the ability to genetically alter specific transcript expression by small inhibitory (si-) and micro (mi-) RNAs are highly useful for the molecular characterization of diseases associated with the transcribed regions. However, the utility of these and other genomic resources are dependent upon having a complete and high quality catalogue of transcribed regions.",
                        "end_date": "2012-12-31",
                        "title": "COMPREHENSIVE CHARACTERIZATION AND CLASSIFICATION OF THE HUMAN TRANSCRIPTOME",
                        "url": "http://projectreporter.nih.gov/project_info_details.cfm?aid=8298287",
                        "uuid": "c68bafc1-dda3-41a9-b889-ec756f0368e1",
                        "schema_version": "1",
                        "start_date": "2007-09-27",
                        "project": "ENCODE",
                        "rfa": "ENCODE2",
                        "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                        "@id": "/awards/U54HG004557/",
                        "@type": [
                            "award",
                            "item"
                        ],
                        "name": "U54HG004557"
                    },
                    "urls": [],
                    "lab": {
                        "status": "CURRENT",
                        "city": "Woodbury",
                        "fax": "516-422-4109",
                        "phone1": "516-422-4105",
                        "uuid": "dfc72c8c-d45c-4acd-979b-49fc93cf3c62",
                        "title": "Thomas Gingeras, CSHL",
                        "phone2": "",
                        "address1": "500 Sunnyside Blvd",
                        "@type": [
                            "lab",
                            "item"
                        ],
                        "institute_name": "Cold Spring Harbor Laboratory",
                        "schema_version": "1",
                        "postal_code": "11797",
                        "state": "NY",
                        "awards": [
                            "/awards/U54HG004557/",
                            "/awards/U54HG007004/"
                        ],
                        "country": "USA",
                        "date_created": "2013-10-02T18:13:24.088370",
                        "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                        "@id": "/labs/thomas-gingeras/",
                        "institute_label": "CSHL",
                        "name": "thomas-gingeras"
                    },
                    "date_created": "2013-10-02T18:20:01.164703",
                    "document_type": "general protocol",
                    "@id": "/documents/7aa32299-cc11-4f07-bdaa-a55de6f51a99/",
                    "@type": [
                        "document",
                        "item"
                    ],
                    "description": "PromoCell Normal Human Aortic Smooth Muscle Cells general protocol"
                }
            ],
            "uuid": "559cc681-09e3-4144-95d9-7c94100126d4",
            "strand_specificity": true,
            "fragmentation_method": "see document",
            "schema_version": "1",
            "lysis_method": "see document",
            "biosample": {
                "accession": "ENCBS000RNA",
                "passage_number": 2,
                "alternate_accessions": [],
                "starting_amount": "6x10^5",
                "lot_id": "8121902.2P",
                "aliases": [
                    "thomas-gingeras:140WC"
                ],
                "rnais": [],
                "submitted_by": {
                    "first_name": "Carrie",
                    "last_name": "Davis",
                    "uuid": "0abbd494-b852-433c-b360-93996f679dae",
                    "title": "Carrie Davis",
                    "submits_for": [
                        "/labs/thomas-gingeras/",
                        "/labs/roderic-guigo/"
                    ],
                    "schema_version": "1",
                    "email": "someone@cshl.edu",
                    "lab": "/labs/thomas-gingeras/",
                    "timezone": "US/Eastern",
                    "@id": "/users/0abbd494-b852-433c-b360-93996f679dae/",
                    "@type": [
                        "user",
                        "item"
                    ],
                    "job_title": "Project Manager"
                },
                "uuid": "c305924f-1058-47bb-af42-259bad767853",
                "biosample_type": "primary cell line",
                "schema_version": "1",
                "note": "Purchased as total RNA",
                "source": {
                    "status": "CURRENT",
                    "name": "promocell",
                    "title": "PromoCell",
                    "url": "http://www.promocell.com",
                    "uuid": "b8e804f7-04f2-4042-8aca-eeeb12bdc6f1",
                    "schema_version": "1",
                    "actions": [
                        {
                            "profile": "/profiles/source.json",
                            "title": "Edit",
                            "href": "",
                            "method": "PUT",
                            "name": "edit"
                        }
                    ],
                    "date_created": "2013-10-02T18:13:25.456978",
                    "@id": "/sources/promocell/",
                    "@type": [
                        "source",
                        "item"
                    ],
                    "description": "PromoCell GmbH"
                },
                "donor": {
                    "status": "CURRENT",
                    "uuid": "807d50f9-3554-426c-a851-b952099e91f0",
                    "organism": {
                        "status": "CURRENT",
                        "name": "human",
                        "scientific_name": "Homo sapiens",
                        "schema_version": "1",
                        "taxon_id": "9606",
                        "date_created": "2013-10-02T18:13:24.361817",
                        "@id": "/organisms/human/",
                        "@type": [
                            "organism",
                            "item"
                        ],
                        "uuid": "7745b647-ff15-4ff3-9ced-b897d4e2983c"
                    },
                    "children": [],
                    "accession": "ENCDO017AAA",
                    "award": "/awards/U41HG006992/",
                    "sex": "male",
                    "parents": [],
                    "schema_version": "1",
                    "alternate_accessions": [
                        "ENCDO117AAA"
                    ],
                    "siblings": [],
                    "lab": "/labs/j-michael-cherry/",
                    "date_created": "2013-10-02T18:18:42.778071",
                    "@id": "/human-donors/807d50f9-3554-426c-a851-b952099e91f0/",
                    "@type": [
                        "human_donor",
                        "donor",
                        "item"
                    ],
                    "ethnicity": "Caucasian",
                    "aliases": [
                        "promocell:8121902"
                    ]
                },
                "pooled_from": [],
                "status": "CURRENT",
                "part_of": [],
                "description": "Normal Human Aortic Smooth Muscle Cells (HAoSMC)",
                "age_units": "year",
                "encode2_dbxrefs": [],
                "life_stage": "adult",
                "constructs": [],
                "treatments": [],
                "award": {
                    "description": "The goal of this proposal is to comprehensively identify all sequence-based functional elements associated with transcribed sequences including both protein coding and non-protein coding sequences, characterizing gene structures including transcription start sites (TSS) polyadenylation sites and alternative transcripts detected in a representative and diverse panel of human cells and tissues. Based on the empirically determined characteristics of the detected transcripts uncovered in this proposal, a classification system for transcribed protein coding and non-protein coding portions of the human transcriptome will be established. Our aims include first to generate a comprehensive set of subcellular compartment-specific long (>200 nucleotides, nts) and short (<200 nts) polyadenylated (polyA+) and non-polyadenylated (polyA-) RNA samples from each of the cell types studied. These RNA samples will be analyzed using: a) high density tiling arrays (5 nucleotides [nt] interrogation resolution for long and short RNAs), b) sequencing (pyrosequencing [454] and clonal single molecule sequencing for short RNAs [Solexa]), c) sequenced paired-end ditags (PETs) for 5' TSS and 3' termination locations for polyA+ transcripts and d) sequenced cap analysis of gene expression (CAGE) tags for 5' TSS of polyA- RNAs. Characterization of full length subcellular compartment-specific transcripts will also be carried out using: 1) a combination of rapid amplification of cDNA ends (RACE), RT-PCR and sequencing, 2) RNA immunoprecipitation (RIP) and 3) in situ immunohistochemistry. These characterization steps will provide additional information concerning the annotated and unannotated RNAs found to be associated with known functional, compartment-specific proteins and their localization in subcellular organelles of known function. The research and health-care community are well positioned to take advantage of a detailed catalog of classified transcribed regions in the human genome. For example, the identification of millions of single nucleotide polymorphism (SNPs) and the ability to genetically alter specific transcript expression by small inhibitory (si-) and micro (mi-) RNAs are highly useful for the molecular characterization of diseases associated with the transcribed regions. However, the utility of these and other genomic resources are dependent upon having a complete and high quality catalogue of transcribed regions.",
                    "end_date": "2012-12-31",
                    "title": "COMPREHENSIVE CHARACTERIZATION AND CLASSIFICATION OF THE HUMAN TRANSCRIPTOME",
                    "url": "http://projectreporter.nih.gov/project_info_details.cfm?aid=8298287",
                    "uuid": "c68bafc1-dda3-41a9-b889-ec756f0368e1",
                    "schema_version": "1",
                    "start_date": "2007-09-27",
                    "project": "ENCODE",
                    "rfa": "ENCODE2",
                    "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                    "@id": "/awards/U54HG004557/",
                    "@type": [
                        "award",
                        "item"
                    ],
                    "name": "U54HG004557"
                },
                "lab": {
                    "status": "CURRENT",
                    "city": "Woodbury",
                    "fax": "516-422-4109",
                    "phone1": "516-422-4105",
                    "uuid": "dfc72c8c-d45c-4acd-979b-49fc93cf3c62",
                    "title": "Thomas Gingeras, CSHL",
                    "phone2": "",
                    "address1": "500 Sunnyside Blvd",
                    "@type": [
                        "lab",
                        "item"
                    ],
                    "institute_name": "Cold Spring Harbor Laboratory",
                    "schema_version": "1",
                    "postal_code": "11797",
                    "state": "NY",
                    "awards": [
                        "/awards/U54HG004557/",
                        "/awards/U54HG007004/"
                    ],
                    "country": "USA",
                    "date_created": "2013-10-02T18:13:24.088370",
                    "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                    "@id": "/labs/thomas-gingeras/",
                    "institute_label": "CSHL",
                    "name": "thomas-gingeras"
                },
                "protocol_documents": [
                    {
                        "status": "CURRENT",
                        "submitted_by": {
                            "first_name": "Carrie",
                            "last_name": "Davis",
                            "uuid": "0abbd494-b852-433c-b360-93996f679dae",
                            "title": "Carrie Davis",
                            "submits_for": [
                                "/labs/thomas-gingeras/",
                                "/labs/roderic-guigo/"
                            ],
                            "schema_version": "1",
                            "email": "someone@cshl.edu",
                            "lab": "/labs/thomas-gingeras/",
                            "timezone": "US/Eastern",
                            "@id": "/users/0abbd494-b852-433c-b360-93996f679dae/",
                            "@type": [
                                "user",
                                "item"
                            ],
                            "job_title": "Project Manager"
                        },
                        "uuid": "11e2d7d3-d43a-4b5a-bf3e-136948efc023",
                        "aliases": [
                            "ENCODE:HAoSMC_PC_8121902.2P_certificate_of_analysis"
                        ],
                        "attachment": {
                            "download": "8121902.2P.pdf",
                            "href": "@@download/attachment/8121902.2P.pdf",
                            "type": "application/pdf"
                        },
                        "schema_version": "1",
                        "references": [],
                        "award": {
                            "description": "The goal of this proposal is to comprehensively identify all sequence-based functional elements associated with transcribed sequences including both protein coding and non-protein coding sequences, characterizing gene structures including transcription start sites (TSS) polyadenylation sites and alternative transcripts detected in a representative and diverse panel of human cells and tissues. Based on the empirically determined characteristics of the detected transcripts uncovered in this proposal, a classification system for transcribed protein coding and non-protein coding portions of the human transcriptome will be established. Our aims include first to generate a comprehensive set of subcellular compartment-specific long (>200 nucleotides, nts) and short (<200 nts) polyadenylated (polyA+) and non-polyadenylated (polyA-) RNA samples from each of the cell types studied. These RNA samples will be analyzed using: a) high density tiling arrays (5 nucleotides [nt] interrogation resolution for long and short RNAs), b) sequencing (pyrosequencing [454] and clonal single molecule sequencing for short RNAs [Solexa]), c) sequenced paired-end ditags (PETs) for 5' TSS and 3' termination locations for polyA+ transcripts and d) sequenced cap analysis of gene expression (CAGE) tags for 5' TSS of polyA- RNAs. Characterization of full length subcellular compartment-specific transcripts will also be carried out using: 1) a combination of rapid amplification of cDNA ends (RACE), RT-PCR and sequencing, 2) RNA immunoprecipitation (RIP) and 3) in situ immunohistochemistry. These characterization steps will provide additional information concerning the annotated and unannotated RNAs found to be associated with known functional, compartment-specific proteins and their localization in subcellular organelles of known function. The research and health-care community are well positioned to take advantage of a detailed catalog of classified transcribed regions in the human genome. For example, the identification of millions of single nucleotide polymorphism (SNPs) and the ability to genetically alter specific transcript expression by small inhibitory (si-) and micro (mi-) RNAs are highly useful for the molecular characterization of diseases associated with the transcribed regions. However, the utility of these and other genomic resources are dependent upon having a complete and high quality catalogue of transcribed regions.",
                            "end_date": "2012-12-31",
                            "title": "COMPREHENSIVE CHARACTERIZATION AND CLASSIFICATION OF THE HUMAN TRANSCRIPTOME",
                            "url": "http://projectreporter.nih.gov/project_info_details.cfm?aid=8298287",
                            "uuid": "c68bafc1-dda3-41a9-b889-ec756f0368e1",
                            "schema_version": "1",
                            "start_date": "2007-09-27",
                            "project": "ENCODE",
                            "rfa": "ENCODE2",
                            "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                            "@id": "/awards/U54HG004557/",
                            "@type": [
                                "award",
                                "item"
                            ],
                            "name": "U54HG004557"
                        },
                        "urls": [],
                        "lab": {
                            "status": "CURRENT",
                            "city": "Woodbury",
                            "fax": "516-422-4109",
                            "phone1": "516-422-4105",
                            "uuid": "dfc72c8c-d45c-4acd-979b-49fc93cf3c62",
                            "title": "Thomas Gingeras, CSHL",
                            "phone2": "",
                            "address1": "500 Sunnyside Blvd",
                            "@type": [
                                "lab",
                                "item"
                            ],
                            "institute_name": "Cold Spring Harbor Laboratory",
                            "schema_version": "1",
                            "postal_code": "11797",
                            "state": "NY",
                            "awards": [
                                "/awards/U54HG004557/",
                                "/awards/U54HG007004/"
                            ],
                            "country": "USA",
                            "date_created": "2013-10-02T18:13:24.088370",
                            "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                            "@id": "/labs/thomas-gingeras/",
                            "institute_label": "CSHL",
                            "name": "thomas-gingeras"
                        },
                        "date_created": "2013-10-02T18:18:56.678820",
                        "document_type": "certificate of analysis",
                        "@id": "/documents/11e2d7d3-d43a-4b5a-bf3e-136948efc023/",
                        "@type": [
                            "document",
                            "item"
                        ],
                        "description": "PromoCell Normal Human Aortic Smooth Muscle Cells certificate of analysis"
                    },
                    {
                        "status": "CURRENT",
                        "submitted_by": {
                            "first_name": "Carrie",
                            "last_name": "Davis",
                            "uuid": "0abbd494-b852-433c-b360-93996f679dae",
                            "title": "Carrie Davis",
                            "submits_for": [
                                "/labs/thomas-gingeras/",
                                "/labs/roderic-guigo/"
                            ],
                            "schema_version": "1",
                            "email": "someone@cshl.edu",
                            "lab": "/labs/thomas-gingeras/",
                            "timezone": "US/Eastern",
                            "@id": "/users/0abbd494-b852-433c-b360-93996f679dae/",
                            "@type": [
                                "user",
                                "item"
                            ],
                            "job_title": "Project Manager"
                        },
                        "uuid": "7aa32299-cc11-4f07-bdaa-a55de6f51a99",
                        "aliases": [
                            "ENCODE:HAoSMC_PC_8121902.2P_general_protocol"
                        ],
                        "attachment": {
                            "download": "SID38242.pdf",
                            "href": "@@download/attachment/SID38242.pdf",
                            "type": "application/pdf"
                        },
                        "schema_version": "1",
                        "references": [],
                        "award": {
                            "description": "The goal of this proposal is to comprehensively identify all sequence-based functional elements associated with transcribed sequences including both protein coding and non-protein coding sequences, characterizing gene structures including transcription start sites (TSS) polyadenylation sites and alternative transcripts detected in a representative and diverse panel of human cells and tissues. Based on the empirically determined characteristics of the detected transcripts uncovered in this proposal, a classification system for transcribed protein coding and non-protein coding portions of the human transcriptome will be established. Our aims include first to generate a comprehensive set of subcellular compartment-specific long (>200 nucleotides, nts) and short (<200 nts) polyadenylated (polyA+) and non-polyadenylated (polyA-) RNA samples from each of the cell types studied. These RNA samples will be analyzed using: a) high density tiling arrays (5 nucleotides [nt] interrogation resolution for long and short RNAs), b) sequencing (pyrosequencing [454] and clonal single molecule sequencing for short RNAs [Solexa]), c) sequenced paired-end ditags (PETs) for 5' TSS and 3' termination locations for polyA+ transcripts and d) sequenced cap analysis of gene expression (CAGE) tags for 5' TSS of polyA- RNAs. Characterization of full length subcellular compartment-specific transcripts will also be carried out using: 1) a combination of rapid amplification of cDNA ends (RACE), RT-PCR and sequencing, 2) RNA immunoprecipitation (RIP) and 3) in situ immunohistochemistry. These characterization steps will provide additional information concerning the annotated and unannotated RNAs found to be associated with known functional, compartment-specific proteins and their localization in subcellular organelles of known function. The research and health-care community are well positioned to take advantage of a detailed catalog of classified transcribed regions in the human genome. For example, the identification of millions of single nucleotide polymorphism (SNPs) and the ability to genetically alter specific transcript expression by small inhibitory (si-) and micro (mi-) RNAs are highly useful for the molecular characterization of diseases associated with the transcribed regions. However, the utility of these and other genomic resources are dependent upon having a complete and high quality catalogue of transcribed regions.",
                            "end_date": "2012-12-31",
                            "title": "COMPREHENSIVE CHARACTERIZATION AND CLASSIFICATION OF THE HUMAN TRANSCRIPTOME",
                            "url": "http://projectreporter.nih.gov/project_info_details.cfm?aid=8298287",
                            "uuid": "c68bafc1-dda3-41a9-b889-ec756f0368e1",
                            "schema_version": "1",
                            "start_date": "2007-09-27",
                            "project": "ENCODE",
                            "rfa": "ENCODE2",
                            "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                            "@id": "/awards/U54HG004557/",
                            "@type": [
                                "award",
                                "item"
                            ],
                            "name": "U54HG004557"
                        },
                        "urls": [],
                        "lab": {
                            "status": "CURRENT",
                            "city": "Woodbury",
                            "fax": "516-422-4109",
                            "phone1": "516-422-4105",
                            "uuid": "dfc72c8c-d45c-4acd-979b-49fc93cf3c62",
                            "title": "Thomas Gingeras, CSHL",
                            "phone2": "",
                            "address1": "500 Sunnyside Blvd",
                            "@type": [
                                "lab",
                                "item"
                            ],
                            "institute_name": "Cold Spring Harbor Laboratory",
                            "schema_version": "1",
                            "postal_code": "11797",
                            "state": "NY",
                            "awards": [
                                "/awards/U54HG004557/",
                                "/awards/U54HG007004/"
                            ],
                            "country": "USA",
                            "date_created": "2013-10-02T18:13:24.088370",
                            "pi": "/users/09d05b87-4d30-4dfb-b243-3327005095f2/",
                            "@id": "/labs/thomas-gingeras/",
                            "institute_label": "CSHL",
                            "name": "thomas-gingeras"
                        },
                        "date_created": "2013-10-02T18:20:01.164703",
                        "document_type": "general protocol",
                        "@id": "/documents/7aa32299-cc11-4f07-bdaa-a55de6f51a99/",
                        "@type": [
                            "document",
                            "item"
                        ],
                        "description": "PromoCell Normal Human Aortic Smooth Muscle Cells general protocol"
                    }
                ],
                "@id": "/biosamples/ENCBS000RNA/",
                "starting_amount_units": "cells",
                "product_id": "C-14053",
                "characterizations": [],
                "url": "http://www.promocell.com/nc/products/human-primary-cells/smooth-muscle-cells/human-aortic-smooth-muscle-cells-haosmc",
                "biosample_term_id": "CL:0002539",
                "age": "21",
                "biosample_term_name": "aortic smooth muscle cell",
                "health_status": "Neg for Bac/Fung/Myc, Neg for HIV-1/HBV/HCV",
                "derived_from": [],
                "date_created": "2013-10-02T18:20:18.076258",
                "organism": "/organisms/human/",
                "@type": [
                    "biosample",
                    "item"
                ]
            },
            "extraction_method": "see document",
            "library_size_selection_method": "see document",
            "status": "CURRENT",
            "nucleic_acid_term_name": "RNA",
            "award": "/awards/U54HG004557/",
            "paired_ended": false,
            "lab": "/labs/thomas-gingeras/",
            "@id": "/libraries/ENCLB000ZZZ/",
            "size_range": ">200",
            "nucleic_acid_term_id": "SO:0000356",
            "date_created": "2013-10-02T18:22:07.529443",
            "@type": [
                "library",
                "item"
            ]
        },
        "date_created": "2013-10-02T18:22:39.193208",
        "@id": "/replicates/f7934dc2-7107-4ee1-9653-9b052a8a8420/",
        "@type": [
            "replicate",
            "item"
        ],
        "aliases": []
    },
    "alternate_accessions": [],
    "output_type": "reads2",
    "date_created": "2013-05-09",
    "submitted_file_name": "../../../../pre-DCC/wgEncodeCshlLongRnaSeq/20130218_promocell_batches1-2_minus_batch1sFASTQ/SID38242_AC1GKKACXX_7_2.txt.gz",
    "@id": "/files/ENCFF001QZP/",
    "@type": [
        "file",
        "item"
    ]
}
