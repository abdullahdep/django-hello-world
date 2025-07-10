from django.shortcuts import render

def global_variables(request):
    return {
        # Site Info
        'site_name': 'Safar Academy',
        'site_description': 'This is a site dedicated to educational resources.',
        'site_keywords': 'education, academy, learning, subjects, courses',
        'site_author': 'John Doe',
        'site_url': 'https://www.safaracademy.com',
        'site_email': 'contact@safaracademy.com',
        'site_phone': '+1 234 567 890',
        'site_address': '123 Main St, Anytown, USA',
        'grades': [9, 10, 11, 12] ,

        
        # Social Links
        'site_facebook': 'https://www.facebook.com/safaracademy',
        'site_twitter': 'https://www.twitter.com/safaracademy',
        'site_instagram': 'https://www.instagram.com/safaracademy',
        'site_linkedin': 'https://www.linkedin.com/company/safaracademy',
        'site_youtube': 'https://www.youtube.com/c/safaracademy',
        'site_pinterest': 'https://www.pinterest.com/safaracademy',
        'site_tiktok': 'https://www.tiktok.com/@safaracademy',
        'site_snapchat': 'https://www.snapchat.com/add/safaracademy',
        'site_whatsapp': 'https://wa.me/1234567890',
        'site_telegram': 'https://t.me/safaracademy',
        'site_discord': 'https://discord.gg/safaracademy',
        'site_reddit': 'https://www.reddit.com/r/safaracademy',
        'site_quora': 'https://www.quora.com/profile/safaracademy',
        'site_github': 'https://github.com/safaracademy',
        
        # Logo
        'logo': 'https://lh3.googleusercontent.com/pw/AP1GczPH1U1q1XyyTn7BQmKTdBEXxxK0SsCqW88OV7VITDEz-nQXA69Gqv5FxBWbisCUJ3Gbw6ALRs7YlAr7d7PJR5k4zNw90n54I6gj_GJ4bwnTRDUCD9LXyOsQLociy6CQ-kIBoRE91_GsXoQe-47Uc1nw=w869-h869-s-no-gm?authuser=0',

        # Subjects Data (Now a dictionary of subjects with descriptions and links)
        'subjects': {
            'English': {
                'description': 'Learn the fundamentals of English language and literature.',
                'anchor': 'login'
            },
            'Mathematics': {
                'description': 'Study algebra, calculus, and more to excel in Mathematics.',
                'anchor': 'https://www.safaracademy.com/subjects/mathematics'
            },
            'Physics': {
                'description': 'Explore the world of Physics, from mechanics to thermodynamics.',
                'anchor': 'https://www.safaracademy.com/subjects/physics'
            },
            'Chemistry': {
                'description': 'Understand the basics of Chemistry, reactions, and lab techniques.',
                'anchor': 'https://www.safaracademy.com/subjects/chemistry'
            },
            'Biology': {
                'description': 'Dive into the world of life sciences, anatomy, and ecology.',
                'anchor': 'https://www.safaracademy.com/subjects/biology'
            },
            'Computer Science': {
                'description': 'Master programming, algorithms, and everything related to computers.',
                'anchor': 'https://www.safaracademy.com/subjects/computer-science'
            },
        },

        # Chapters Data (Detailed structure for each subject and grade)
        'chapters': {
            'mathematics': {
                9: [
                    {
                        'name': 'Algebra and Functions',
                        'slug': 'algebra-and-functions',
                        'topics': [
                            'Quadratic Equations',
                            'Linear Equations in Two Variables',
                            'Polynomials',
                            'Coordinate Geometry'
                        ]
                    },
                    {
                        'name': 'Number Systems',
                        'slug': 'number-systems',
                        'topics': [
                            'Real Numbers',
                            'Irrational Numbers',
                            'Rational Numbers',
                            'Decimal Representation'
                        ]
                    },
                    {
                        'name': 'Geometry',
                        'slug': 'geometry',
                        'topics': [
                            'Triangles and Congruence',
                            'Circles',
                            'Areas and Perimeters',
                            'Surface Areas and Volumes'
                        ]
                    }
                ],
                10: [
                    {
                        'name': 'Trigonometry',
                        'slug': 'trigonometry',
                        'topics': [
                            'Introduction to Trigonometry',
                            'Trigonometric Ratios',
                            'Heights and Distances',
                            'Applications'
                        ]
                    },
                    {
                        'name': 'Statistics and Probability',
                        'slug': 'statistics-and-probability',
                        'topics': [
                            'Mean, Median, Mode',
                            'Probability Theory',
                            'Data Handling',
                            'Graphical Representation'
                        ]
                    }
                ],
                11: [
                    {
                        'name': 'Advanced Calculus',
                        'slug': 'advanced-calculus',
                        'topics': [
                            'Limits and Derivatives',
                            'Applications of Derivatives',
                            'Integrals',
                            'Differential Equations'
                        ]
                    },
                    {
                        'name': 'Complex Numbers',
                        'slug': 'complex-numbers',
                        'topics': [
                            'Introduction to Complex Numbers',
                            'Algebraic Properties',
                            'Polar Form',
                            'Applications in 2D Geometry'
                        ]
                    }
                ],
                12: [
                    {
                        'name': 'Linear Algebra',
                        'slug': 'linear-algebra',
                        'topics': [
                            'Matrices and Determinants',
                            'Vector Algebra',
                            'Linear Programming',
                            'Three Dimensional Geometry'
                        ]
                    },
                    {
                        'name': 'Advanced Integration',
                        'slug': 'advanced-integration',
                        'topics': [
                            'Definite Integrals',
                            'Applications in Physics',
                            'Area Under Curves',
                            'Differential Equations'
                        ]
                    }
                ]
            },
            'biology': {
                9: [
                    {
                        'name': 'Chapter 1: The Science Of Biology',
                        'slug': 'Chapter 1: The Science Of Biology',
                        'topics': [
                            '1.1 Biology and its Branches',
                            '1.2 Relation of Biology with Other Sciences',
                            '1.3 Careers in Biology',
                            '1.4 Quranic Instructions to Reveal the Study of Life',
                            '1.5 Science as a Collaborative Feild',
                            '1.6 Scientific Method',
                            '1.7 Theory and Law/Principle',
                            '1.8 Malaria -An Example of Biological Method',
                        ]
                    },
                    {
                        'name': 'Chapter 2: Biodiversity',
                        'slug': 'matChapter 2: Biodiversityter',
                        'topics': [
                            '2.1 Biodiversity',
                            '2.2 Classification',
                            '2.3 Taxonomic Ranks',
                            '2.4 History of Classification',
                            '2.5 Domains of Living Organisms',
                            '2.6 Classification of Domain Eukarya',
                            '2.7 Status of Virus in Classification',
                            '2.8 Bionomial Nomenclature'
                        ]
                    },
                    {
                        'name': 'Chapter 3: The Cell',
                        'slug': 'Chapter 3: The Cell',
                        'topics': [
                            '3.1 Cell',
                            '3.2 Structure of Cell',
                            '3.3 Structural Advantages of Plant and Animal Cells',
                            '3.4 Cell Specilization',
                            '3.5 Stem Cells',
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 4: Cell Cycle',
                        'slug': 'Chapter 4: Cell Cycle',
                        'topics': [
                            '4.1 Cell Cycle',
                            '4.2 Mitosis',
                            '4.3 Meiosis',
                            '4.4 Comparison between Mitosis and Meiosis',
                        ]
                    },
                    {
                        'name': 'Chapter 5: Tissues, Organs, and Organ Systems',
                        'slug': 'Chapter 5: Tissues, Organs, and Organ Systems',
                        'topics': [
                            '5.1 Levels of Organization',
                            '5.2 Organs and Organ Systems in Plants ',
                            '5.3 Organs and Organ Systems in Humans',
                            '5.4 Homeostatis'
                        ]
                    },
                    {
                        'name': 'Chapter 6: Biomolecules',
                        'slug': 'Chapter 6: Biomolecules',
                        'topics': [
                            '6.1 Biomolecules',
                            '6.2 Carbohydrates',
                            '6.3 Proteins',
                            '6.4 Lipids',
                            '6.5 Nucleic Acids',
                            '6.6 The Working of DNA and RNA'
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 7: Enzymes',
                        'slug': 'Chapter 7: Enzymes',
                        'topics': [
                            '7.1 Metabolism',
                            '7.2 Enzymes',
                            '7.3 Mechanism of Enzyme Action',
                            '7.4 Factors that Affect the Activity of Enzymes',
                            '7.5 Enzyme Inhibition'
                        ]
                    },
                    {
                        'name': 'Chapter 8: Bioenergetics',
                        'slug': 'Chapter 8: Bioenergetics',
                        'topics': [
                            '8.1 ATP: The Cell\'s Energy Currency',
                            '8.2 Photosynthesis',
                            '8.3 Cellular Respiration',
                            
                        ]
                    },
                    {
                        'name': 'Chapter 9: Plant Physiology',
                        'slug': 'Chapter 9: Plant Physiology',
                        'topics': [
                            '9.1 Nutrition in Plants',
                            '9.2 Transport in Plants',
                            '9.3 Transpiration',
                            '9.4 Transport of Water and Salt in Plants',
                            '9.5 Translocation of Food in Plant',
                            '9.6 Gaseous Exchange in Plants',
                            '9.7 Mechanisms for Excretion in Plants',
                            '9.8 Osmotic Adjustments in Plants'
                        ]
                    },
                    {
                        'name': 'Chapter 10: Respiration in Plants',
                        'slug': 'Chapter 10: Respiration in Plants',
                        'topics': [
                            '10.1 Types of Asexual Reproduction',
                            '10.2  Artificial Propagation',
                            '10.3 Sexual Reproduction in Plants',
                            
                        ]
                    },
                    {
                        'name': 'Chapter 11: Biostatistics',
                        'slug': 'Chapter 11: Biostatistics',
                        'topics': [
                            '11.1 Introduction of Biostatistics',
                            '11.2 Mean, Median,and Mode',
                            '11.3 Bar Chart'                        ]
                    }
                ],
                10: [
  {
    "name": "Chapter 10: Gaseous Exchange",
    "slug": "gaseous-exchange",
    "topics": [
      "10.1 Gaseous Exchange In Plants",
      "10.2 Gaseous Exchange In Humans",
      "10.3 Respiratory Disorders"
    ]
  },
  {
    "name": "Chapter 11: Homeostasis",
    "slug": "homeostasis",
    "topics": [
      "11.1 Homeostasis In Plants",
      "11.2 Homeostasis In Humans",
      "11.3 The Urinary System Of Humans",
      "11.4 Disorders Of Kidney"
    ]
  },
  {
    "name": "Chapter 12: Coordination and Control",
    "slug": "coordination-and-control",
    "topics": [
      "12.1 Types Of Coordination",
      "12.2 Human Nervous System",
      "12.3 Receptors In Humans",
      "12.4 Endocrine System",
      "12.5 Disorders Of Nervous System"
    ]
  },
  {
    "name": "Chapter 13: Support and Movement",
    "slug": "support-and-movement",
    "topics": [
      "13.1 Human Skeleton",
      "13.2 Types Of Joints",
      "13.3 Muscles And Movement",
      "13.4 Disorders Of Skeletal System"
    ]
  },
  {
    "name": "Chapter 14: Reproduction",
    "slug": "reproduction",
    "topics": [
      "14.1 Reproduction",
      "14.2 Methods Of Asexual Reproduction",
      "14.3 Sexual Reproduction In Plants",
      "14.4 Sexual Reproduction In Animals"
    ]
  },
  {
    "name": "Chapter 15: Inheritance",
    "slug": "inheritance",
    "topics": [
      "15.1 Introduction To Genetics",
      "15.2 Chromosomes And Genes",
      "15.3 Mendel’s Laws Of Inheritance",
      "15.4 Co-Dominance And Incomplete Dominance",
      "15.5 Variations And Evolution"
    ]
  },
  {
    "name": "Chapter 16: Man and His Environment",
    "slug": "man-and-his-environment",
    "topics": [
      "16.1 Levels Of Biological Selection",
      "16.2 Flow Of Materials And Energy In Ecosystem",
      "16.3 Interactions In Ecosystems",
      "16.4 Ecosystem Balance And Human Impact",
      "16.5 Pollution; Consequenses And Control",
      "16.6 Conservation Of Nature"
    ]
  },
  {
    "name": "Chapter 17: Biotechnology",
    "slug": "biotechnology",
    "topics": [
      "17.1 Introduction Of Biotechnology",
      "17.2 Fermentation",
      "17.3 Genetic Engineering",
      "17.4 Single-Cell Protein"
    ]
  },
  {
    "name": "Chapter 18: Pharmacology",
    "slug": "pharmacology",
    "topics": [
      "18.1 Medicinal Drugs",
      "18.2 Addictive Drugs",
      "18.3 Antibiotics And Vaccines"
    ]
  }
]
,
                11: [
    {
        "name": "Chapter 1: Biodiversity and Classification",
        "slug": "Chapter 1: Biodiversity and Classification",
        "topics": [
            "1.1 Three-Domain System of Classification",
            "1.2 Taxonomic Hierarchy",
            "1.4 Classification of Kingdom Animalia",
            "1.5 Classification of Vertebrates",
            "1.6 Classification of Viruses",
            "1.7 Biodiversity",
            "1.8 Species and Speciation"
        ]
    },
    {
        "name": "Chapter 2: Bacteria and Viruses",
        "slug": "Chapter 2: Bacteria and Viruses",
        "topics": [
            "2.1 Structure of Bacteria",
            "2.2 Endospore Formation in Bacteria",
            "2.3 Motility in Bacteria",
            "2.5 Flagella",
            "2.6 Bacteria: Ecology and Diversity",
            "2.7 Importance of Bacteria",
            "2.8 Normal Flora",
            "2.9 Virus"
        ]
    },
    {
        "name": "Chapter 3: Cells and Subcellular Organelles",
        "slug": "Chapter 3: Cells and Subcellular Organelles",
        "topics": [
            "3.1 Cells - The Basic Unit of Life",
            "3.2 Cell Theory",
            "3.3 Microscopy",
            "3.4 Structure of Cell",
            "3.5 Prokaryotic and Eukaryotic Cells",
            "3.6 Cell Signalling",
            "3.7 Membrane Transport Mechanisms",
            "3.8 Stem Cells"
        ]
    },
    {
        "name": "Chapter 4: Biomolecules",
        "slug": "Chapter 4: Biomolecules",
        "topics": [
            "4.1 Biological Molecules",
            "4.2 Types of Bonds in Biology",
            "4.3 Condensation (Synthesis) and Hydrolysis",
            "4.4 Importance of Water",
            "4.5 Carbohydrates",
            "4.6 Proteins",
            "4.7 Lipids",
            "4.8 Nucleic Acids",
            "4.9 Conjugated Molecules"
        ]
    },
    {
        "name": "Chapter 5: Enzymes",
        "slug": "Chapter 5: Enzymes",
        "topics": [
            "5.1 Enzymes",
            "5.2 Cofactors and Coenzymes",
            "5.3 Mechanism of Enzyme Action",
            "5.4 Factors Affecting the Rate of Enzyme Action",
            "5.6 Enzyme Inhibition",
            "5.7 Classification of Enzymes"
        ]
    },
    {
        "name": "Chapter 6: Bioenergetics",
        "slug": "Chapter 6: Bioenergetics",
        "topics": [
            "6.1 Photosynthesis",
            "6.2 Cellular Respiration",
            "6.3 Photorespiration"
        ]
    },
    {
        "name": "Chapter 7: Structural and Computational Biology",
        "slug": "Chapter 7: Structural and Computational Biology",
        "topics": [
            "7.1 Applications of Structural Biology",
            "7.2 X-Ray Crystallography",
            "7.3 Computational Biology",
            "7.4 Sequence Homology"
        ]
    },
    {
        "name": "Chapter 8: Plant Physiology",
        "slug": "Chapter 8: Plant Physiology",
        "topics": [
            "8.1 Nutrition in Plants",
            "8.2 Gas Exchange in Plants",
            "8.3 Support in Plants",
            "8.4 Water Potential",
            "8.5 Transport of Water in Plants",
            "8.6 Translocation of Food in Plants",
            "8.7 Growth in Plants",
            "8.8 Osmoregulation in Plants",
            "8.9 Thermoregulation in Plants",
            "8.10 Movements in Plants",
            "8.11 Photoperiodism",
            "8.12 Vernalisation"
        ]
    },
    {
        "name": "Chapter 9: Human Digestive System",
        "slug": "Chapter 9: Human Digestive System",
        "topics": [
            "9.1 Anatomy & Physiology of Digestive System"
        ]
    },
    {
        "name": "Chapter 10: Human Respiratory System",
        "slug": "Chapter 10: Human Respiratory System",
        "topics": [
            "10.1 Respiratory System of Man",
            "10.2 Transport of Gases",
            "10.3 Respiratory Pigments",
            "10.4 Respiratory Disorders"
        ]
    },
    {
        "name": "Chapter 11: Human Circulatory System",
        "slug": "Chapter 11: Human Circulatory System",
        "topics": [
            "11.1 Structure and Functioning of Heart",
            "11.2 Blood Vessels",
            "11.3 Blood Pressure",
            "11.4 Cardiovascular Disorders",
            "11.5 Lymphatic System of Human"
        ]
    },
    {
        "name": "Chapter 12: Human Skeletal and Muscular Systems",
        "slug": "Chapter 12: Human Skeletal and Muscular Systems",
        "topics": [
            "12.1 Bones and Cartilage",
            "12.2 Disorders of Skeletal System",
            "12.3 Muscles"
        ]
    }
]
,
                12:  [ 
    {
        "name": "Chapter 15: Homeostasis",
        "slug": "Chapter 15: Homeostasis",
        "topics": [
            "15.1 Concepts in Homeostasis",
            "15.2 Osmoregulation",
            "15.3 Excretion",
            "15.4 Excretion in Representative Animals",
            "15.5 Excretion in Vertebrates",
            "15.6 Kidney Problems and Cures",
            "15.7 Thermoregulation",
            "15.8 Thermoregulation in Mammals (Human)"
        ]
    },
    {
        "name": "Chapter 16: Support And Movement",
        "slug": "Chapter 16: Support And Movement",
        "topics": [
            "16.1 Support in Plants",
            "16.2 Movements in Plants",
            "16.3 Support and Movements in Animals",
            "16.4 Human Skeleton",
            "16.5 Deformities of Skeleton",
            "16.6 Repair of Broken Bones",
            "16.7 Muscles",
            "16.8 Controlling the Actin - Myosin Interaction by Ca++ ion",
            "16.9 Arrangement of Skeletal Muscles for Movement of Skeleton",
            "16.10 Locomotion in Protoctista and Invertebrates",
            "16.11 Locomotion and Skeleton in Vertebrates",
            "16.12 Evolutionary Changes in the Arrangement of Bones and Related Mode of Locomotion in Major Groups of Vertebrates"
        ]
    },
    {
        "name": "Chapter 17: Coordination And Control",
        "slug": "Chapter 17: Coordination And Control",
        "topics": [
            "17.1 Introduction",
            "17.2 Coordination in Plants - Control through Hormones",
            "17.3 Plant Movements",
            "17.4 Responses to Environmental Stresses in Plants",
            "17.5 Defense Against Pathogens in Plants",
            "17.6 Biological Clocks and Circadian Rhythms",
            "17.7 Plant Growth Regulatory Substances",
            "17.8 Coordination in Animals",
            "17.9 Working of Sensory Receptors with Special Reference to Skin",
            "17.10 Nerve Impulse",
            "17.11 Synapse",
            "17.12 Evolution of Nervous System",
            "17.13 Central Nervous System (CNS)",
            "17.14 Peripheral Nervous System (PNS)",
            "17.15 Autonomic Nervous System",
            "17.16 Nervous Disorder",
            "17.17 Effect of Drugs on Coordination",
            "17.18 Chemical Coordination",
            "17.19 Endocrine Glands of Mammals",
            "17.20 Behaviour"
        ]
    },
    {
        "name": "Chapter 18: Reproduction",
        "slug": "Chapter 18: Reproduction",
        "topics": [
            "18.1 Introduction",
            "18.2 Reproduction in Plants",
            "18.3 Reproduction in Animals",
            "18.4 Tissue Culturing and Cloning",
            "18.5 Sexual Reproduction",
            "18.6 Sexually Transmitted Diseases (STD)"
        ]
    },
    {
        "name": "Chapter 19: Growth and Development",
        "slug": "Chapter 19: Growth and Development",
        "topics": [
            "19.1 Growth and Development in Plants",
            "19.2 Growth Correlations",
            "19.3 Concept of Differentiation"
        ]
    },
    {
        "name": "Chapter 20: Chromosomes and DNA",
        "slug": "Chapter 20: Chromosomes and DNA",
        "topics": [
            "20.1 Types of Chromosomes",
            "20.2 Composition of Chromosome",
            "20.3 The Chromosomal Theory of Inheritance",
            "20.4 DNA as Hereditary Material",
            "20.5 Chemical Nature of DNA",
            "20.6 DNA Replication",
            "20.7 What is a Gene?",
            "20.8 One-Gene / One-Polypeptide Hypothesis",
            "20.9 Cells Use RNA to Make Protein",
            "20.10 Genetic Code"
        ]
    },
    {
        "name": "Chapter 21: Cell Cycle",
        "slug": "Chapter 21: Cell Cycle",
        "topics": [
            "21.1 Introduction",
            "21.2 Interphase",
            "21.3 Cancer (Uncontrolled Cell Division)",
            "21.4 Meiotic Errors (Non-Disjunction)",
            "21.5 Necrosis and Apoptosis"
        ]
    },
    {
        "name": "Chapter 22: Variation and Genetics",
        "slug": "Chapter 22: Variation and Genetics",
        "topics": [
            "22.1 Genes, Alleles and Gene Pool",
            "22.2 Mendel's Laws of Inheritance",
            "22.3 Mendel's Interpretations",
            "22.4 Dihybrid and Dihybrid Cross",
            "22.5 Dominance Relations",
            "22.6 MN Blood Type or Blood Group System",
            "22.7 Epistasis",
            "22.8 Continuously Varying Trait",
            "22.9 Crossing Over",
            "22.10 Sex Determination",
            "22.11 Sex Linkage",
            "22.12 Diabetes Mellitus and Its Genetic Basis"
        ]
    },
    {
        "name": "Chapter 23: Biotechnology",
        "slug": "Chapter 23: Biotechnology",
        "topics": [
            "23.1 Recombinant DNA Technology",
            "23.2 Genomic Library",
            "23.3 The Polymerase Chain Reaction",
            "23.4 The Human Genome Project",
            "23.5 Biotechnology Products",
            "23.6 Gene Therapy",
            "23.7 Tissue Culture",
            "23.8 Genetic Engineering of Plants",
            "23.9 Agricultural Plants with Improved Trait"
        ]
    },
    {
        "name": "Chapter 24: Evolution",
        "slug": "Chapter 24: Evolution",
        "topics": [
            "24.1 Concept of Evolution vs Special Creation",
            "24.2 Evolution from Prokaryotes to Eukaryotes",
            "24.3 Inheritance of Acquired Characteristics",
            "24.4 Neo-Darwinism - The Modern Evolutionary Synthesis",
            "24.5 Population, Gene Pool, Allele and Genotype Frequencies",
            "24.6 Endangered Species"
        ]
    },
    {
        "name": "Chapter 25: Ecosystem",
        "slug": "Chapter 25: Ecosystem",
        "topics": [
            "25.1 Ecosystem",
            "25.2 Components of Ecosystem",
            "25.3 Succession",
            "25.4 Biogeochemical Cycles"
        ]
    },
    {
        "name": "Chapter 26: Some Major Ecosystems",
        "slug": "Chapter 26: Some Major Ecosystems",
        "topics": [
            "26.1 Aquatic or Hydrospheric Ecosystem",
            "26.2 Terrestrial or Lithospheric Ecosystem",
            "26.3 Some Major Ecosystems in Pakistan"
        ]
    }
]
            }
            ,
            'english':{
                10:[
  {
    "name": "Hazrat Muhammad (SAW) an Embodiment of Justice",
    "slug": "Hazrat Muhammad (SAW) an Embodiment of Justice",
    "topic": "Hazrat Muhammad (SAW) an Embodiment of Justice"
  },
  {
    "name": "Chinese New Year",
    "slug": "Chinese New Year",
    "topic": "Chinese New Year"
  },
  {
    "name": "Try Again",
    "slug": "Try Again",
    "topic": "Try Again"
  },
  {
    "name": "First Aid",
    "slug": "First Aid",
    "topic": "First Aid"
  },
  {
    "name": "The Rain",
    "slug": "The Rain",
    "topic": "The Rain"
  },
  {
    "name": "Television vs Newspapers",
    "slug": "Television vs Newspapers",
    "topic": "Television vs Newspapers"
  },
  {
    "name": "Little by Little One Walks Far!",
    "slug": "Little by Little One Walks Far!",
    "topic": "Little by Little One Walks Far!"
  },
  {
    "name": "Peace",
    "slug": "Peace",
    "topic": "Peace"
  },
  {
    "name": "Selecting the Right Career",
    "slug": "Selecting the Right Career",
    "topic": "Selecting the Right Career"
  },
  {
    "name": "A World Without Books",
    "slug": "A World Without Books",
    "topic": "A World Without Books"
  },
  {
    "name": "Great Expectations",
    "slug": "Great Expectations",
    "topic": "Great Expectations"
  },
  {
    "name": "Population Growth and World Food Supplies",
    "slug": "Population Growth and World Food Supplies",
    "topic": "Population Growth and World Food Supplies"
  },
  {
    "name": "Faithfulness",
    "slug": "Faithfulness",
    "topic": "Faithfulness"
  }
]
,   
                12:[
  {
    "name": "Chapter 1: Khatm-un-Nabiyeen Hazrat Muhammad (SAW)",
    "slug": "chapter-1-khatm-un-nabiyeen-hazrat-muhammad-saw",
    "topics": ["Khatm-un-Nabiyeen Hazrat Muhammad (SAW)"]
  },
  {
    "name": "Chapter 2: Responsibility of the Youth in Nation-Building",
    "slug": "chapter-2-responsibility-of-the-youth-in-nation-building",
    "topics": ["Responsibility of the Youth in Nation-Building"]
  },
  {
    "name": "Chapter 3: A Bird Came Down the Walk (Poem)",
    "slug": "chapter-3-a-bird-came-down-the-walk-poem",
    "topics": ["A Bird Came Down the Walk (Poem)"]
  },
  {
    "name": "Chapter 4: Team Moon",
    "slug": "chapter-4-team-moon",
    "topics": ["Team Moon"]
  },
  {
    "name": "Chapter 5: Impacts of Global Warming on Pakistan",
    "slug": "chapter-5-impacts-of-global-warming-on-pakistan",
    "topics": ["Impacts of Global Warming on Pakistan"]
  },
  {
    "name": "Chapter 6: The Echoing Green (Poem)",
    "slug": "chapter-6-the-echoing-green-poem",
    "topics": ["The Echoing Green (Poem)"]
  },
  {
    "name": "Chapter 7: What You Do is What You Are",
    "slug": "chapter-7-what-you-do-is-what-you-are",
    "topics": ["What You Do is What You Are"]
  },
  {
    "name": "Chapter 8: Clean Water",
    "slug": "chapter-8-clean-water",
    "topics": ["Clean Water"]
  },
  {
    "name": "Chapter 9: Freedom (Poem)",
    "slug": "chapter-9-freedom-poem",
    "topics": ["Freedom (Poem)"]
  },
  {
    "name": "Chapter 10: The Punishment of Shapesh, the Persian, on Khipil, the Builder",
    "slug": "chapter-10-the-punishment-of-shapesh-the-persian-on-khipil-the-builder",
    "topics": ["The Punishment of Shapesh, the Persian, on Khipil, the Builder"]
  },
  {
    "name": "Chapter 11: Those Winter Sundays (Poem)",
    "slug": "chapter-11-those-winter-sundays-poem",
    "topics": ["Those Winter Sundays (Poem)"]
  },
  {
    "name": "Chapter 12: The Impact of AI on Society, Human Relationships, and Ethics",
    "slug": "chapter-12-the-impact-of-ai-on-society-human-relationships-and-ethics",
    "topics": ["The Impact of AI on Society, Human Relationships, and Ethics"]
  },
  {
    "name": "Chapter 13: Ruba'iyat (Poem)",
    "slug": "chapter-13-rubaiyat-poem",
    "topics": ["Ruba'iyat (Poem)"]
  },
  {
    "name": "Chapter 14: The End of the Beginning",
    "slug": "chapter-14-the-end-of-the-beginning",
    "topics": ["The End of the Beginning"]
  }
]

            }
            ,
            'physics': {
                9: [
                    {
                        'name': 'Chapter 1:Physical Quantities and Measurements',
                        'slug': 'Chapter 1:Physical Quantities and Measurements',
                        'topics': [
                            '1.1 Physical and Non-Physical Quantities',
                            '1.2 Base and Derived Physical Quantities',
                            '1.3 International System of Units',
                            '1.4 Scientific Notation',
                            '1.5 Length Measuring Instruments',
                            '1.6 Mass Measuring Instruments',
                            '1.7 Time Measuring Instruments',
                            '1.8 Volume Measuring Instruments',
                            '1.9 Errors in Measurements',
                            '1.10 Uncertainity in a Measurement',
                            '1.11 Significant Figures',
                            '1.12 Precision and Accuracy',
                            '1.13 Rounding off the digits',
                        ]
                    },
                    {
                        'name': 'Chapter 2: Kinematics',
                        'slug': 'Chapter 2: Kinematics',
                        'topics': [
                            '2.1 Scalars and Vectors',
                            '2.2 Rest and Motion',
                            '2.3 Types of Motion',
                            '2.4 Distance and Displacement',
                            '2.5 Speed and Velocity',
                            '2.6 Acceleration',
                            '2.7 Graphical Analysis of Motion',
                            '2.8 Gradient of a Distance-Time Graph',
                            '2.9 Speed-Time Graph',
                            '2.10 Gradient of a Speed-Time Graph',
                            '2.11 Area Under Speed-Time Graph',
                            '2.12 Solving Problems for Motion Under Gravity',
                            '2.13 Free Fall Acceleration'

                        ]
                    },
                    {
                        'name': 'Chapter 3: Dynamics',
                        'slug': 'Chapter 3: Dynamics',
                        'topics': [
                            '3.1 Concept of Force',
                            '3.2 Fundamental Forces',
                            '3.3 Forces in a Free- Body Diagram',
                            '3.4 Newton’s Laws of Motion',
                            '3.5 Limitations of Newton’s Laws of Motion',
                            '3.6 Mass and Weight',
                            '3.7 Mechanical and Electronic Balances',
                            '3.8 Friction',
                            '3.9 Momentum and Impulse',
                            '3.10 Principle of Conservation of Momentum',

                           
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 4: Turning Effects of Forces',
                        'slug': 'Chapter 4: Turning Effects of Forces',
                        'topics': [
                            '4.1 Cell Cycle',
                            '4.1 Like and Unlike Parallel Forces',
                            '4.2 Addition of Forces',
                            '4.3 Turning Effect of a Force',
                            '4.4 Resolution of Vectors',
                            '4.5 Determination of a Force from its Prependicular Components',
                            '4.6 Principle of Moments',
                            '4.7 Centre of Gravity and Centre of Mass',
                            '4.8 Equilibrium',
                            '4.9 Conditions of Equilibrium',
                            '4.10 States of Equilibrium',
                            '4.11 Improvement of Stability',
                            '4.12 Application of Stability in Real Life',
                            '4.13 Centripetal Force'
                                    ]
                    },
                    {
                        'name': 'Chapter 5: Work, Energy and Power',
                        'slug': 'Chapter 5: Work, Energy and Power',
                        'topics': [
                            '5.1 Work' ,
                            '5.2 Energy',
                            '5.3 Conservation of Energy',
                            '5.4 Sources of Energy',
                            '5.5 Renewable and Non-Renewable Sources',
                            '5.6 The Advantages and Disadvantages of methods of Energy production',
                            '5.7 Power',
                            '5.8 Efficiency',

                        ]
                    },
                    {
                        'name': 'Chapter 6: Mechanical Properties of Matter',
                        'slug': 'Chapter 6: Mechanical Properties of Matter',
                        'topics': [
                            '6.1 Deformation of solids',
                            '6.2 Hooke’s law',
                            '6.3 Density',
                            '6.4 Pressure',
                            '6.5 Pressure in Liquids',
                            '6.6 Atmospheric Pressure',
                            '6.7 Measurement of Atmospheric Pressure',
                            '6.8 Measurement of Pressure by Manometer',
                            '6.9 Pascal’s Law'
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 7: Thermal Properties of Matter',
                        'slug': 'Chapter 7: Thermal Properties of Matter',
                        'topics': [
                            '7.1 Kinetic Molecular Theory of Matter',
                            '7.2 Temperature and Heat',
                            '7.3 Thermometers',
                            '7.4 Sensitivity, Range and Linearity of Thermometers',
                            '7.5 Structure of A Liquid-in-Glass Thermometer'
                        ]
                    },
                    {
                        'name': 'Chapter 8: Magnetism',
                        'slug': 'Chapter 8: Magnetism',
                        'topics': [
                            '8.1 Magnetic Materials',
                            '8.2 Properties of Magnets',
                            '8.3 Induced Magnetism',
                            '8.4 Temporary and Permanent Magnets ',
                            '8.5 Magnetic Fields',
                            '8.6 Uses of Permanent Magnets',
                            '8.7 Electromagnets',
                            '8.8 Domain Theory of Magnetism',
                            '8.9 Magnetization and Demagnetization',
                            '8.10 Applications of Magnets in Recording Technology',
                            '8.11 Soft Iron as Magnetic Shield'
                            
                        ]
                    },
                    {
                        'name': 'Chapter 9: Nature of Science',
                        'slug': 'Chapter 9: Nature of Science',
                        'topics': [
                            '9.1 Scope of Physics',
                            '9.2 Branches of Physics',
                            '9.3 Interdisciplinary Nature of Physics',
                            '9.4 Interdisciplinary Research',
                            '9.5 Scientific Method',
                            '9.6 Scientific Base of Technologies and Engineering'

                        ]
                    }
                ],
                10:[
  {
    "name": "Unit 10: Simple Harmonic Motion and Waves",
    "slug": "simple-harmonic-motion-and-waves",
    "topics": [
      "10.1 SIMPLE HARMONIC MOTION (SHM)",
      "10.2 DAMPED OSCILLATIONS",
      "10.3 WAVE MOTION",
      "10.4 TYPES OF MECHANICAL WAVES",
      "10.5 RIPPLE TANK"
    ]
  },
  {
    "name": "Unit 11: Sound",
    "slug": "sound",
    "topics": [
      "11.1 SOUND WAVES",
      "11.2 CHARACTERISTICS OF SOUND",
      "11.3 REFLECTION (ECHO) OF SOUND",
      "11.4 SPEED OF SOUND",
      "11.5 NOISE POLLUTION",
      "11.6 IMPORTANCE OF ACOUSTICS",
      "11.7 AUDIBLE FREQUENCY RANGE",
      "11.8 ULTRASOUND"
    ]
  },
  {
    "name": "Unit 12: Geometrical Optics",
    "slug": "geometrical-optics",
    "topics": [
      "12.1 REFLECTION OF LIGHT",
      "12.2 SPHERICAL MIRRORS",
      "12.3 IMAGE LOCATION BY SPHERICAL MIRROR FORMULA",
      "12.4 REFRACTION OF LIGHT",
      "12.5 TOTAL INTERNAL REFLECTION",
      "12.6 APPLICATIONS OF TOTAL INTERNAL REFLECTION",
      "12.7 REFRACTION THROUGH PRISM",
      "12.8 LENSES",
      "12.9 IMAGE FORMATION BY LENSES",
      "12.10 IMAGE LOCATION BY LENS EQUATION",
      "12.11 APPLICATIONS OF LENSES",
      "12.12 SIMPLE MICROSCOPE",
      "12.13 COMPOUND MICROSCOPE",
      "12.14 TELESCOPE GEOMETRICAL OPTICS",
      "12.15 THE HUMAN EYE",
      "12.16 DEFECTS OF VISION"
    ]
  },
  {
    "name": "Unit 13: Electrostatics",
    "slug": "electrostatics",
    "topics": [
      "13.1 PRODUCTION OF ELECTRIC CHARGES",
      "13.2 ELECTROSTATIC INDUCTION",
      "13.3 ELECTROSCOPE",
      "13.4 COULOMB'S LAW",
      "13.5 ELECTRIC FIELD AND ELECTRIC FIELD INTENSITY",
      "13.6 ELECTROSTATIC POTENTIAL",
      "13.7 CAPACITORS AND CAPACITANCE",
      "13.8 DIFFERENT TYPES OF CAPACITORS",
      "13.9 APPLICATIONS OF ELECTROSTATICS",
      "13.10 SOME HAZARDS OF STATIC ELECTRICITY"
    ]
  },
  {
    "name": "Unit 14: Current Electricity",
    "slug": "current-electricity",
    "topics": [
      "14.1 ELECTRIC CURRENT",
      "14.2 POTENTIAL DIFFERENCE",
      "14.3 ELECTROMOTIVE FORCE (e.m.f)",
      "14.4 OHM'S LAW",
      "14.5 V-I Characteristics of Ohmic and Non Ohmic Conductors",
      "14.6 FACTORS AFFECTING RESISTANCE",
      "14.7 CONDUCTORS",
      "14.8 INSULATORS",
      "14.9 COMBINATION OF RESISTORS",
      "14.10 ELECTRICAL ENERGY AND JOULE'S LAW",
      "14.11 ELECTRIC POWER",
      "14.12 DIRECT CURRENT AND ALTERNATING CURRENT",
      "14.13 HAZARDS OF ELECTRICITY",
      "14.14 SAFE USE OF ELECTRICITY IN HOMES"
    ]
  },
  {
    "name": "Unit 15: Electromagnetism",
    "slug": "electromagnetism",
    "topics": [
      "15.1 MAGNETIC EFFECTS OF A STEADY CURRENT",
      "15.2 FORCE ON A CURRENT CARRYING CONDUCTOR PLACED IN A MAGNETIC FIELD",
      "15.3 TURNING EFFECT ON A CURRENT-CARRYING COIL IN A MAGNETIC FIELD",
      "15.4 D. C. MOTOR",
      "15.5 ELECTROMAGNETIC INDUCTION",
      "15.6 Direction of induced e.m.f. – Lenz’s Law",
      "15.7 A.C. GENERATOR",
      "15.8 MUTUAL INDUCTION",
      "15.9 TRANSFORMER",
      "15.10 HIGH VOLTAGE TRANSMISSION"
    ]
  },
  {
    "name": "Unit 16: Basic Electronics",
    "slug": "basic-electronics",
    "topics": [
      "16.1 THERMIONIC EMISSION",
      "16.2 INVESTIGATING THE PROPERTIES OF ELECTRONS",
      "16.3 CATHODE-RAY OSCILLOSCOPE (C.R.O)",
      "16.4 ANALOGUE AND DIGITAL ELECTRONICS",
      "16.5 BASIC OPERATION OF DIGITAL ELECTRONICS – LOGIC GATES",
      "16.6 AND OPERATION",
      "16.7 OR OPERATION",
      "16.8 NOT OPERATION",
      "16.9 NAND GATE",
      "16.10 NOR GATE",
      "16.11 USES OF LOGIC GATES"
    ]
  },
  {
    "name": "Unit 17: Information and Communication Technology",
    "slug": "information-and-communication-technology",
    "topics": [
      "17.1 INFORMATION AND COMMUNICATION TECHNOLOGY",
      "17.2 COMPONENTS OF COMPUTER BASED INFORMATION SYSTEM (CBIS)",
      "17.3 FLOW OF INFORMATION",
      "17.4 TRANSMISSION OF ELECTRICAL SIGNAL THROUGH WIRES",
      "17.5 TRANSMISSION OF RADIOWAVES THROUGH SPACE",
      "17.6 TRANSMISSION OF LIGHT SIGNALS THROUGH OPTICAL FIBRES",
      "17.7 INFORMATION STORAGE DEVICES",
      "17.8 APPLICATIONS OF COMPUTER WORD PROCESSING",
      "17.9 INTERNET",
      "17.10 RISKS OF ICT TO SOCIETY AND THE ENVIRONMENT"
    ]
  },
  {
    "name": "Unit 18: Atomic and Nuclear Physics",
    "slug": "atomic-and-nuclear-physics",
    "topics": [
      "18.1 ATOM AND ATOMIC NUCLEUS",
      "18.2 NATURAL RADIOACTIVITY",
      "18.3 BACKGROUND RADIATIONS",
      "18.4 NUCLEAR TRANSMUTATIONS",
      "18.5 HALF-LIFE AND ITS MEASUREMENT",
      "18.6 RADIOISOTOPES AND THEIR USES",
      "18.7 FISSION REACTION",
      "18.8 NUCLEAR FUSION",
      "18.9 HAZARDS OF RADIATIONS AND SAFETY MEASURES"
    ]
  }
]
,
                11: [
  {
    "name": "Chapter 1: Measurements",
    "slug": "Chapter 1: Measurements",
    "topics": [
      "1.1 Physical Quantities and their Units",
      "1.2 International System of Units",
      "1.3 Uncertainty in Measurement",
      "1.4 Use of Significant Figures",
      "1.5 Precision and Accuracy",
      "1.6 Assessment of Total Uncertainty in the Final Result",
      "1.7 Dimensions of Physical Quantities"
    ]
  },
  {
    "name": "Chapter 2: Force and Motion",
    "slug": "Chapter 2: Force and Motion",
    "topics": [
      "2.1 Scalars",
      "2.2 Vectors",
      "2.3 Product of Two Vectors",
      "2.4 Equations of Motion",
      "2.5 Motion Under Gravity",
      "2.6 Projectile Motion",
      "2.7 Momentum",
      "2.8 Elastic and Inelastic Collisions",
      "2.9 Elastic Collision in Two Dimensions",
      "2.10 Inelastic Collision in One Dimension",
      "2.11 Inelastic Collision in Two Dimensions",
      "2.12 Rocket Propulsion"
    ]
  },
  {
    "name": "Chapter 3: Circular and Rotational Motion",
    "slug": "Chapter 3: Circular and Rotational Motion",
    "topics": [
      "3.1 Angular Measurements",
      "3.2 Centripetal Force",
      "3.3 Artificial Satellites",
      "3.4 Moment of Inertia",
      "3.5 Angular Momentum",
      "3.6 Law of Conservation of Angular Momentum"
    ]
  },
  {
    "name": "Chapter 4: Work, Energy and Power",
    "slug": "Chapter 4: Work, Energy and Power",
    "topics": [
      "4.1 Work done by a Constant Force",
      "4.2 Work done by a Variable Force",
      "4.3 Conservative and Non-Conservative Forces",
      "4.4 Power",
      "4.5 Energy",
      "4.6 Escape Velocity",
      "4.7 Work-Energy Theorem",
      "4.8 Interconversion of Potential Energy and Kinetic Energy"
    ]
  },
  {
    "name": "Chapter 5: Solids and Fluid Dynamics",
    "slug": "Chapter 5: Solids and Fluid Dynamics",
    "topics": [
      "5.1 Classification of Solids",
      "5.2 Mechanical Properties of Solids",
      "5.3 Stress, Strain and Young's Modulus",
      "5.4 Determination of Young's Modulus of a Wire",
      "5.5 Elastic Deformation, Plastic Deformation and Elastic Limit",
      "5.6 Strain Energy in Deformed Materials",
      "5.7 Archimedes' Principle and Floatation",
      "5.8 Steady, Non-Viscous and Ideal Fluid",
      "5.9 Equation of Continuity",
      "5.10 Increase in Flow Velocity",
      "5.11 Bernoulli's Equation",
      "5.12 Uses of Bernoulli's Principle",
      "5.13 Viscous Drag and Stokes' Law",
      "5.14 Terminal Velocity",
      "5.15 Real Fluids are Viscous Fluids",
      "5.16 Superfluids"
    ]
  },
  {
    "name": "Chapter 6: Heat and Thermodynamics",
    "slug": "Chapter 6: Heat and Thermodynamics",
    "topics": [
      "6.1 Assumptions of the Kinetic Theory of Gases",
      "6.2 Internal Energy",
      "6.3 Work and Heat",
      "6.4 First Law of Thermodynamics",
      "6.5 Reversible and Irreversible Processes",
      "6.6 Heat Engine",
      "6.7 Second Law of Thermodynamics",
      "6.8 Carnot Engine and Carnot's Theorem",
      "6.9 Refrigerator",
      "6.10 Entropy"
    ]
  },
  {
    "name": "Chapter 7: Waves and Vibrations",
    "slug": "Chapter 7: Waves and Vibrations",
    "topics": [
      "7.1 Waves",
      "7.2 Principle of Superposition of Waves",
      "7.3 Interference and its Types",
      "7.4 Stationary Waves and their Formation",
      "7.5 Stationary Waves in a Stretched String",
      "7.6 Stationary Waves in Air Columns",
      "7.7 Experiment Demonstrating Stationary Waves using Microwaves",
      "7.8 Diffraction of Waves",
      "7.9 Beats",
      "7.10 Intensity (I) of a Wave",
      "7.11 Doppler Effect",
      "7.12 Application of Doppler Effect"
    ]
  },
  {
    "name": "Chapter 8: Physical Optics and Gravitational Waves",
    "slug": "Chapter 8: Physical Optics and Gravitational Waves",
    "topics": [
      "8.1 Polarization of Light",
      "8.2 Types of Polarization",
      "8.3 Production and Detection of Plane Polarized Light",
      "8.4 Polarized Light by the Method of Reflection",
      "8.5 Malus's Law",
      "8.6 Gravitational Waves (GWs)",
      "8.7 Interferometer"
    ]
  },
  {
    "name": "Chapter 9: Electrostatics and Current Electricity",
    "slug": "Chapter 9: Electrostatics and Current Electricity",
    "topics": [
      "9.1 Coulomb's Law",
      "9.2 Electric Field Strength",
      "9.3 Electric Flux",
      "9.4 Gauss's Law",
      "9.5 Electric Potential",
      "9.6 Electron Volt",
      "9.7 Motion of Charged Particles in a Uniform Electric Field",
      "9.8 Path of a Charged Particle",
      "9.9 Shielding from External Electric Field",
      "9.10 Electric Current",
      "9.11 Current Through a Conductor",
      "9.12 Ohm's Law",
      "9.13 Resistivity and its Dependence upon Temperature",
      "9.14 Electrical Power",
      "9.15 Electromotive Force (EMF) and Potential Difference",
      "9.16 Kirchhoff's Rules",
      "9.17 Wheatstone Bridge",
      "9.18 Potentiometer",
      "9.19 Use of a Galvanometer",
      "9.20 Thermistors",
      "9.21 Light Dependent Resistors"
    ]
  },
  {
    "name": "Chapter 10: Electromagnetism",
    "slug": "Chapter 10: Electromagnetism",
    "topics": [
      "10.1 Force on a Current-Carrying Conductor in a Uniform Magnetic Field",
      "10.2 Magnetic Flux and Flux Density",
      "10.3 Magnetic Flux Linkage",
      "10.4 Motion of a Charged Particle in a Magnetic Field",
      "10.5 Velocity Selector",
      "10.6 Induced EMF Faraday's Law",
      "10.7 Lenz's Law and Direction of Induced EMF",
      "10.8 Factors Affecting EMF",
      "10.9 Ferrofluids",
      "10.10 A Seismometer"
    ]
  },
  {
    "name": "Chapter 11: Special Theory of Relativity",
    "slug": "Chapter 11: Special Theory of Relativity",
    "topics": [
      "11.1 Relative Motion",
      "11.2 Frames of Reference",
      "11.3 Special Theory of Relativity",
      "11.4 The Equivalence Between Mass and Energy",
      "11.5 Space-Time in Relativity"
    ]
  },
  {
    "name": "Chapter 12: Nuclear and Particle Physics",
    "slug": "Chapter 12: Nuclear and Particle Physics",
    "topics": [
      "12.1 Structure and Properties of the Nucleus",
      "12.2 Fundamental Forces of Nature",
      "12.3 Matter and Anti-Matter",
      "12.4 Radioactivity",
      "12.5 Fundamental Particles",
      "12.6 Quarks",
      "12.7 Higgs Boson",
      "12.8 Conservation Laws",
      "12.9 The Asymmetry of Matter and Anti-Matter in the Universe",
      "12.10 Most of the Matter in the Observable Universe is Plasma",
      "12.11 The Theories about the Forces between the Masses of Particles",
      "12.12 The Standard Model"
    ]
  }
]
,
                12: [
    {
        "name": "Unit 12: Electrostatics",
        "slug": "unit-12-electrostatics",
        "topics": [
            "12.1 Coulomb's Law",
            "12.2 Fields of Force",
            "12.3 Electric Field Lines",
            "12.4 Applications of Electrostatics",
            "12.5 Electric Flux",
            "12.6 Electric Flux Through a Surface Enclosing a Charge",
            "12.7 Gauss's Law",
            "12.8 Applications of Gauss's Law",
            "12.9 Electric Potential",
            "12.10 Electron Volt",
            "12.11 Electric and Gravitational Forces (A Comparison)",
            "12.12 Charge on an Electron by Millikan's Method",
            "12.13 Capacitor",
            "12.14 Capacitance of a Parallel Plate Capacitor",
            "12.15 Electric Polarization of Dielectrics",
            "12.16 Energy Stored in a Capacitor",
            "12.17 Charging and Discharging a Capacitor"
        ]
    },
    {
        "name": "Unit 13: Current Electricity",
        "slug": "unit-13-current-electricity",
        "topics": [
            "13.1 Electric Current",
            "13.2 Source of Current",
            "13.3 Effects of Current",
            "13.4 Ohm's Law",
            "13.5 Resistivity and its Dependence upon Temperature",
            "13.6 Colour Code for Carbon Resistances",
            "13.7 Electrical Power and Dissipation in Resistor Power",
            "13.8 Electromotive Force (EMF) and Potential Difference",
            "13.9 Kirchhoff's Rules",
            "13.10 Wheatstone Bridge",
            "13.11 Potentiometer"
        ]
    },
    {
        "name": "Unit 14: Electromagnetism",
        "slug": "unit-14-electromagnetism",
        "topics": [
            "14.1 Magnetic Field Due to Current in a Long Straight Wire",
            "14.2 Force on a Current Carrying Conductor in a Uniform Magnetic Field",
            "14.3 Magnetic Flux and Flux Density",
            "14.4 Ampere's Law and Determination of Flux Density B",
            "14.5 Force on a Moving Charge in a Magnetic Field",
            "14.6 Motion of Charged Particle in an Electric and Magnetic Field",
            "14.7 Determination of e/m of an Electron",
            "14.8 Lenses",
            "14.9 Cathode Ray Oscilloscope",
            "14.10 Galvanometer",
            "14.11 AVO Meter-Multimeter"
        ]
    },
    {
        "name": "Unit 15: Electromagnetic Induction",
        "slug": "unit-15-electromagnetic-induction",
        "topics": [
            "15.1 Induced EMF and Induced Current",
            "15.2 Motional EMF",
            "15.3 Faraday's Law and Induced EMF",
            "15.4 Lenz's Law and Direction of Induced EMF",
            "15.5 Mutual Induction",
            "15.6 Self Induction",
            "15.7 Energy Stored in an Inductor",
            "15.8 Alternating Current Generator",
            "15.9 D.C. Generator",
            "15.10 Back Motor Effect in Generators",
            "15.11 D.C. Motor",
            "15.12 Back EMF Effect in Motors",
            "15.13 Transformer"
        ]
    },
    {
        "name": "Unit 16: Alternating Current",
        "slug": "unit-16-alternating-current",
        "topics": [
            "16.1 Alternating Current",
            "16.2 A.C. Circuits",
            "16.3 A.C. Through a Resistor",
            "16.4 A.C. Through a Capacitor",
            "16.5 A.C. Through an Inductor",
            "16.6 Impedance",
            "16.7 R-C and R-L Series Circuits",
            "16.8 Power in A.C. Circuits",
            "16.9 Series Resonance Circuit",
            "16.10 Parallel Resonance Circuit",
            "16.11 Three Phase A.C. Supply",
            "16.12 Principle of Metal Detectors",
            "16.13 Choke",
            "16.14 Electromagnetic Waves",
            "16.15 Principle of Generation, Transmission and Reception of Electromagnetic Waves",
            "16.16 Modulation Waves"
        ]
    },
    {
        "name": "Unit 17: Physics of Solids",
        "slug": "unit-17-physics-of-solids",
        "topics": [
            "17.1 Classification of Solids",
            "17.2 Mechanical Properties of Solids",
            "17.3 Electrical Properties of Solids",
            "17.4 Superconductors",
            "17.5 Magnetic Properties of Solids"
        ]
    },
    {
        "name": "Unit 18: Electronics",
        "slug": "unit-18-electronics",
        "topics": [
            "18.1 Brief Review of p-n Junction and its Characteristics",
            "18.2 Rectification",
            "18.3 Specially Designed p-n Junctions",
            "18.4 Transistors",
            "18.5 Transistor as an Amplifier",
            "18.6 Transistor as a Switch",
            "18.7 Operational Amplifier",
            "18.8 Op-Amp as Inverting Amplifier",
            "18.9 Op-Amp as Non-Inverting Amplifier",
            "18.10 Op-Amp as a Comparator",
            "18.11 Comparator as a Night Switch",
            "18.12 Digital Systems",
            "18.13 Fundamental Logic Gates",
            "18.14 Other Logic Gates",
            "18.15 Applications of Gates in Control Systems"
        ]
    },
    {
        "name": "Unit 19: Dawn of Modern Physics",
        "slug": "unit-19-dawn-of-modern-physics",
        "topics": [
            "19.1 Relative Motion",
            "19.2 Frames of Reference",
            "19.3 Special Theory of Relativity",
            "19.4 Black Body Radiation",
            "19.5 Interaction of Electromagnetic Radiation with Matter",
            "19.6 Annihilation of Matter",
            "19.7 Wave Nature of Particles",
            "19.8 Uncertainty Principle"
        ]
    },
    {
        "name": "Unit 20: Atomic Spectra",
        "slug": "unit-20-atomic-spectra",
        "topics": [
            "20.1 Atomic Spectra",
            "20.2 Bohr's Model of the Hydrogen Atom",
            "20.3 Inner Shell Transitions and Characteristic X-Rays",
            "20.4 Uncertainty Within the Atom",
            "20.5 Laser"
        ]
    },
    {
        "name": "Unit 21: Nuclear Physics",
        "slug": "unit-21-nuclear-physics",
        "topics": [
            "21.1 Atomic Nucleus",
            "21.2 Isotopes",
            "21.3 Mass Defect and Binding Energy",
            "21.4 Radioactivity",
            "21.5 Half Life",
            "21.6 Interaction of Radiation with Matter",
            "21.7 Radiation Detectors",
            "21.8 Nuclear Reactions",
            "21.9 Nuclear Fission",
            "21.10 Fusion Reaction",
            "21.11 Radiation Exposure",
            "21.12 Biological Effects of Radiation",
            "21.13 Biological and Medical Uses of Radiation",
            "21.14 Basic Forces of Nature",
            "21.15 Building Blocks of Matter"
        ]
    }
]


            },
            'computer-science': {
                9:[
    {
        "name": "Chapter 1: Introduction to Systems",
        "slug": "Chapter 1: Introduction to Systems",
        "topics": [
            "1.1 Theory of Systems",
            "1.2 Types of Systems",
            "1.3 System and Science",
            "1.4 Computer as a System",
            "1.5 The Architecture of von Neumann Computers",
            "1.6 Computing Systems"
        ]
    },
    {
        "name": "Chapter 2: Number Systems",
        "slug": "Chapter 2: Number Systems",
        "topics": [
            "2.1 Numbering Systems",
            "2.2 Data Representation in Computing Systems",
            "2.3 Storing Real Values in Computer Memory",
            "2.4 Binary Arithmetic Operations",
            "2.5 Common Text Encoding Schemes",
            "2.6 Storing Images, Audios, and Videos in Computer"
        ]
    },
    {
        "name": "Chapter 3: Digital Systems and Logic Design",
        "slug": "Chapter 3: Digital Systems and Logic Design",
        "topics": [
            "3.1 Basics of Digital Systems",
            "3.2 Boolean Algebra and Logic Gates",
            "3.3 Simplification of Boolean Functions",
            "3.4 Creating Logic Diagrams",
            "3.5 Application of Digital Logic"
        ]
    },
    {
        "name": "Chapter 4: System Troubleshooting",
        "slug": "Chapter 4: System Troubleshooting",
        "topics": [
            "4.1 Systems Troubleshooting",
            "4.2 Troubleshooting Strategies"
        ]
    },
    {
        "name": "Chapter 5: Software Systems",
        "slug": "Chapter 5: Software Systems",
        "topics": [
            "5.1 Software",
            "5.2 Introduction to System Software",
            "5.3 Application Software"
        ]
    },
    {
        "name": "Chapter 6: Introduction to Computer Networks",
        "slug": "Chapter 6: Introduction to Computer Networks",
        "topics": [
            "6.1 Network as a System",
            "6.2 Fundamental Concepts in Data Communication",
            "6.3 Networking Devices",
            "6.4 Network Topologies",
            "6.5 Transmission Modes",
            "6.6 The OSI Networking Model",
            "6.7 IPv4 and IPv6",
            "6.8 Protocols and Network Services",
            "6.9 Network Security",
            "6.10 Types of Networks",
            "6.11 Real World Application of Computer Network",
            "6.12 Standard Protocols in TCP/IP Communications",
            "6.13 Network Security Methods"
        ]
    },
    {
        "name": "Chapter 7: Computational Thinking",
        "slug": "Chapter 7: Computational Thinking",
        "topics": [
            "7.1 Definition of Computational Thinking",
            "7.2 Principles of Computational Thinking",
            "7.3 Algorithm Designs Method",
            "7.4 Algorithmic Activities",
            "7.5 Dry Run",
            "7.6 Introduction to LARP (Logic of Algorithms for Resolution of Problems)"
        ]
    },
    {
        "name": "Chapter 8: Web Development with HTML, CSS and JavaScript",
        "slug": "Chapter 8: Web Development with HTML, CSS and JavaScript",
        "topics": [
            "8.1 Web Development",
            "8.2 Basic Components of Web Development",
            "8.3 Getting Started with HTML",
            "8.4 HTML Basic Structure",
            "8.5 Creating Content with HTML",
            "8.6 Styling with CSS",
            "8.7 Introduction to JavaScript",
            "8.8 Developing and Debugging"
        ]
    },
    {
        "name": "Chapter 9: Data Science and Data Gathering",
        "slug": "Chapter 9: Data Science and Data Gathering",
        "topics": [
            "9.1 Data",
            "9.2 Data Types",
            "9.3 Organising and Analysing Data",
            "9.4 Data Types",
            "9.5 Data Storage Techniques",
            "9.6 Data Visualization",
            "9.7 Data PreProcessing and Analysis",
            "9.8 Collaborative Tools and Cloud Storage",
            "9.9 Introduction to Data Science",
            "9.10 Big Data and its Applications"
        ]
    },
    {
        "name": "Chapter 10: Emerging Technologies in Computer Science",
        "slug": "Chapter 10: Emerging Technologies in Computer Science",
        "topics": [
            "10.1 Introduction to Artificial Intelligence (AI)",
            "10.2 AI Algorithms and Techniques",
            "10.3 Introduction to Internet of Things (IoT)",
            "10.4 Implications and Future of Emerging Technologies"
        ]
    },
    {
        "name": "Chapter 11: Ethical, Social, and Legal Concerns in Computer Usage",
        "slug": "Chapter 11: Ethical, Social, and Legal Concerns in Computer Usage",
        "topics": [
            "11.1 Responsible Computer Usage",
            "11.2 Safe and Secure Operation of Digital Platforms",
            "11.3 Best Practices in Online Behavior",
            "11.4 Legal and Ethical Frameworks",
            "11.5 Intellectual Property Rights",
            "11.6 Responsible Internet Use",
            "11.7 Impact of Computing on Society"
        ]
    },
    {
        "name": "Chapter 12: Entrepreneurship in Digital Age",
        "slug": "Chapter 12: Entrepreneurship in Digital Age",
        "topics": [
            "12.1 Entrepreneurship",
            "12.2 Entrepreneurship in Digital Landscape",
            "12.3 Digital Tools and Platform",
            "12.4 Business Idea Generation",
            "12.5 Developing Business Plans",
            "12.6 Ethical and Sustainable Entrepreneurship"
        ]
    }
],

                10:[
  {
    "name": "Unit 1: Introduction to Programming",
    "slug": "introduction-to-programming",
    "topics": [
      "1.1 Programming Environment",
      "1.2 Programming Basics",
      "1.3 Constants and Variables"
    ]
  },
  {
    "name": "Unit 2: User Interface",
    "slug": "user-interface",
    "topics": [
      "2.1 Input/Output (I/O) Functions",
      "2.2 Operators"
    ]
  },
  {
    "name": "Unit 3: Conditional Logic",
    "slug": "conditional-logic",
    "topics": [
      "3.1 Control Statements",
      "3.2 Selection Statements"
    ]
  },
  {
    "name": "Unit 4: Data and Repetition",
    "slug": "data-and-repetition",
    "topics": [
      "4.1 Data Structures",
      "4.2 Loop Structures"
    ]
  },
  {
    "name": "Unit 5: Function",
    "slug": "function",
    "topics": [
      "5.1 Functions"
    ]
  }
]
,
                11:[
    {
        "name": "Unit 1: Introduction to Software Development",
        "slug": "software-development",
        "topics": [
            "1.1 Software Development",
            "1.2 Introduction to Software Development Life Cycle (SDLC)",
            "1.3 Software Development Methodologies",
            "1.4 Project Planning and Management",
            "1.5 Graphical Representation of Software Systems",
            "1.6 Introduction to Design Patterns",
            "1.7 Software Debugging and Testing",
            "1.8 Software Development Tools"
        ]
    },
    {
        "name": "Unit 2: Python Programming",
        "slug": "python-programming",
        "topics": [
            "2.1 Introduction to Python Programming",
            "2.2 Basic Python Syntax and Structure",
            "2.3 Operators and Expressions",
            "2.4 Control Structures",
            "2.5 Python Modules and Built-in Data Structures",
            "2.6 Built-in Data Structures",
            "2.7 Modular Programming in Python",
            "2.8 Object-Oriented Programming in Python",
            "2.9 Advanced Python Concepts",
            "2.10 Testing and Debugging in Python"
        ]
    },
    {
        "name": "Unit 3: Algorithms and Problem Solving",
        "slug": "algorithms-problem-solving",
        "topics": [
            "3.1 Understanding Computational Problems",
            "3.2 Algorithms for Problem Solving",
            "3.3 Problem Solvability and Complexity",
            "3.4 Algorithm Analysis",
            "3.5 Algorithm Efficiency and Scalability",
            "3.6 Algorithm Design Techniques",
            "3.7 Commonly Used Algorithms"
        ]
    },
    {
        "name": "Unit 4: Computational Structures",
        "slug": "computational-structures",
        "topics": [
            "4.1 Primitive Computational Structures",
            "4.2 Choosing the Right Data Structure for the Problem",
            "4.3 Combining Computational Structures for Complex Problems"
        ]
    },
    {
        "name": "Unit 5: Data Analytics",
        "slug": "data-analytics",
        "topics": [
            "5.1 Model Building",
            "5.2 Basic Statistical Concepts",
            "5.3 Data Collection and Preparation",
            "5.4 Building Statistical Models",
            "5.5 Introduction to Data Visualization",
            "5.6 Tools for Data Visualization"
        ]
    },
    {
        "name": "Unit 6: Emerging Technologies",
        "slug": "emerging-technologies",
        "topics": [
            "6.1 Definition and Overview of Emerging Technologies",
            "6.2 Cloud Computing",
            "6.3 Applications and Implications of Cloud Computing",
            "6.4 Introduction to Blockchain Technology",
            "6.5 Applications and Implications of Blockchain",
            "6.6 Future Trends and Innovations"
        ]
    },
    {
        "name": "Unit 7: Legal and Ethical Aspects of Computing Systems",
        "slug": "legal-ethical-computing",
        "topics": [
            "7.1 Understanding Terms of Use",
            "7.2 Privacy and Security Threats",
            "7.3 The Digital Divide and Its Impacts",
            "7.4 Safe and Responsible Information Utilization",
            "7.5 Computing's Impact on Individuals and Society",
            "7.6 Digital Citizenship and Ethical Considerations"
        ]
    },
    {
        "name": "Unit 8: Online Research and Digital Literacy",
        "slug": "online-research-digital-literacy",
        "topics": [
            "8.1 Introduction to Online Research and Digital Literacy",
            "8.2 Formulating Research Inquiries",
            "8.3 Utilizing Digital Resources",
            "8.4 Research Ethics",
            "8.5 Understanding Intellectual Property"
        ]
    },
    {
        "name": "Unit 9: Entrepreneurship in the Digital Age",
        "slug": "entrepreneurship-digital-age",
        "topics": [
            "9.1 Introduction to Design Thinking and Business Solutions",
            "9.2 Creating a Business Plan",
            "9.3 Collecting Market Insights",
            "9.4 Developing Effective Marketing and Sales Strategies",
            "9.5 Financial Concepts for Business",
            "9.6 Communication and Storytelling Skills",
            "9.7 Collaboration and Iteration",
            "9.8 Innovation and Creativity"
        ]
    }
]
,
                12:[
  {
    "name": "Unit 1: Data Basics",
    "slug": "unit-1-data-basics",
    "topics": [
      "1.1 Overview",
      "1.2 Traditional File System",
      "1.3 Databases",
      "1.4 Database Management System"
    ]
  },
  {
    "name": "Unit 2: Basic Concepts and Terminology of Databases",
    "slug": "unit-2-basic-concepts-and-terminology-of-databases",
    "topics": [
      "2.1 Overview",
      "2.2 Attributes, Rows, and Tables",
      "2.3 Relation or Table",
      "2.4 Views",
      "2.5 Indexes",
      "2.6 Keys",
      "2.7 The User",
      "2.8 The Data Administrator",
      "2.9 The Database Administrator"
    ]
  },
  {
    "name": "Unit 3: Database Design Process",
    "slug": "unit-3-database-design-process",
    "topics": [
      "3.1 Overview",
      "3.2 Data Modeling",
      "3.3 Database Design",
      "3.4 Implementation"
    ]
  },
  {
    "name": "Unit 4: Data Integrity and Normalization",
    "slug": "unit-4-data-integrity-and-normalization",
    "topics": [
      "4.1 Overview"
    ]
  },
  {
    "name": "Unit 5: Introduction to Microsoft Access",
    "slug": "unit-5-introduction-to-microsoft-access",
    "topics": [
      "5.1 Overview",
      "5.2 Database Window",
      "5.3 MS-Access Application Window",
      "5.4 Database Objects"
    ]
  },
  {
    "name": "Unit 6: Table and Query",
    "slug": "unit-6-table-and-query",
    "topics": [
      "6.1 Overview",
      "6.2 Table Design View",
      "6.3 Table Creation",
      "6.4 Modifying a Table",
      "6.5 Print a Datasheet",
      "6.6 Table Relationships",
      "6.7 Sorting and Filtering",
      "6.8 Introduction to Queries",
      "6.9 Performing Calculation in a Query"
    ]
  },
  {
    "name": "Unit 7: Microsoft Access Forms and Reports",
    "slug": "unit-7-microsoft-access-forms-and-reports",
    "topics": [
      "7.1 Overview",
      "7.2 Adding Records Using a Form",
      "7.3 List and Combo Boxes",
      "7.4 Check Boxes and Radio Buttons",
      "7.5 Subform",
      "7.6 Drag-and-Drop Method",
      "7.7 Reports",
      "7.8 Linking",
      "7.9 Creating a Switchboard in Access",
      "7.10 Keyboard Shortcuts"
    ]
  },
  {
    "name": "Unit 8: Getting Started with C",
    "slug": "unit-8-getting-started-with-c",
    "topics": [
      "8.1 Overview",
      "8.2 Developing a C Program (A Stepwise Approach)",
      "8.3 Basic Structure of a C Program",
      "8.4 Common Programming Errors",
      "8.5 Programming Languages"
    ]
  },
  {
    "name": "Unit 9: Elements of C",
    "slug": "unit-9-elements-of-c",
    "topics": [
      "9.1 Overview",
      "9.2 Keywords",
      "9.4 Constants",
      "9.5 Data Type",
      "9.6 Operators in C",
      "9.7 Expression",
      "9.8 Comments"
    ]
  },
  {
    "name": "Unit 10: Input/Output",
    "slug": "unit-10-input-output",
    "topics": [
      "10.1 Overview",
      "10.2 scanf Function",
      "10.3 Character Input"
    ]
  },
  {
    "name": "Unit 11: Decision Constructs",
    "slug": "unit-11-decision-constructs",
    "topics": [
      "11.1 Overview",
      "11.2 If Statements",
      "11.3 Use of Logical Operators",
      "11.4 Switch Statement",
      "11.5 Coordinational Operator",
      "11.6 Case Study: Locating a Point in the Coordinate Plane"
    ]
  },
  {
    "name": "Unit 12: Loop Constructs",
    "slug": "unit-12-loop-constructs",
    "topics": [
      "12.1 Overview",
      "12.2 While Statement",
      "12.3 Do-While Loop",
      "12.4 Nested Loop",
      "12.5 Goto Statement"
    ]
  },
  {
    "name": "Unit 13: Function in C",
    "slug": "unit-13-function-in-c",
    "topics": [
      "13.1 Overview",
      "13.2 Importance of Function",
      "13.3 Types of Functions",
      "13.4 Writing Function in C",
      "13.5 Function Prototype",
      "13.6 Calling a Function",
      "13.7 Local Variables and Their Scope",
      "13.8 Global Variables and Their Scopes",
      "13.9 Functions Without Argument",
      "13.10 Functions That Return a Value and Accept Arguments"
    ]
  },
  {
    "name": "Unit 14: File Handling in C",
    "slug": "unit-14-file-handling-in-c",
    "topics": [
      "14.1 Overview",
      "14.2 The Stream",
      "14.3 Newline and EOF Marker",
      "14.4 Opening a File",
      "14.5 Closing a File",
      "14.6 Reading and Writing Characters to a File"
    ]
  }
]

            },
            'chemistry': {
                9: [
    {
        "name": "Chapter 1: Fundamentals of Chemistry",
        "slug": "Chapter 1: Fundamentals of Chemistry",
        "topics": [
            "1.1 What is Chemistry?",
            "1.2 States of Matter",
            "1.3 Element, Compound and Mixture",
            "1.4 Allotropic Forms of Substances",
            "1.5 Difference Between Element, Compound and Mixture",
            "1.6 Solution, Colloidal Solution and Suspension",
            "1.7 Formation of Unsaturated and Saturated Solutions",
            "1.8 Effects of Temperature on Saturated Solutions"
        ]
    },
    {
        "name": "Chapter 2: Structure of Atoms",
        "slug": "Chapter 2: Structure of Atoms",
        "topics": [
            "2.1 Structure of Atom",
            "2.2 Atomic Number and Mass Number",
            "2.3 Isotopes and Their Masses",
            "2.4 Relative Atomic Mass"
        ]
    },
    {
        "name": "Chapter 3: Periodic Table and Periodicity of Properties",
        "slug": "Chapter 3: Periodic Table and Periodicity of Properties",
        "topics": [
            "3.1 Why Does Atom Form Chemical Bonds",
            "3.2 Chemical Bonds",
            "3.3 Metallic Bonds",
            "3.4 Electropositive Character of Metals",
            "3.5 Electronegative Character of Non-Metals",
            "3.6 Compare the Properties of Ionic and Covalent Compounds",
            "3.7 Intermolecular Forces of Attraction",
            "3.8 Nature of Bonding and Properties"
        ]
    },
    {
        "name": "Chapter 4: Structure of Molecules",
        "slug": "Chapter 4: Structure of Molecules",
        "topics": [
            "4.1 Chemical Formula",
            "4.2 Empirical Formula",
            "4.3 Chemical Formula of Binary Ionic Compounds",
            "4.4 Chemical Formula of Compounds",
            "4.5 Deduce the Molecular Formula from the Structural Formula",
            "4.6 Avogadro's Number (Na)",
            "4.7 The Mole and Molar Mass",
            "4.8 Chemical Equation and Chemical Reactions",
            "4.9 Calculations Based on Chemical Equations"
        ]
    },
    {
        "name": "Chapter 5: Physical States of Matter",
        "slug": "Chapter 5: Physical States of Matter",
        "topics": [
            "5.1 System and Surrounding",
            "5.2 Enthalpy",
            "5.3 Exothermic and Endothermic Reactions",
            "5.4 How Does a Reaction Take Place?",
            "5.5 Aerobic and Anaerobic Respiration"
        ]
    },
    {
        "name": "Chapter 6: Solutions",
        "slug": "Chapter 6: Solutions",
        "topics": [
            "6.1 Reversible and Irreversible Changes",
            "6.2 Dynamic Equilibrium",
            "6.3 Changing Physical Conditions of a Chemical Reaction"
        ]
    },
    {
        "name": "Chapter 7: Electrochemistry",
        "slug": "Chapter 7: Electrochemistry",
        "topics": [
            "7.1 Acids and Bases",
            "7.2 Different Concepts of Acids and Bases",
            "7.3 Bronsted-Lowry Concepts of Acids and Bases",
            "7.4 Properties of Acids and Bases",
            "7.5 Acid Rain and Its Effects"
        ]
    },
    {
        "name": "Chapter 8: Periodic Table and Periodicity",
        "slug": "Chapter 8: Periodic Table and Periodicity",
        "topics": [
            "8.1 Modern Periodic Table",
            "8.2 Salient Features of Modern Periodic Table",
            "8.3 Similarities in the Chemical Properties of Elements in the Same Group",
            "8.4 Variation of Periodic Properties in Periods and Groups",
            "8.5 Metallic Character and Reactivity"
        ]
    },
    {
        "name": "Chapter 9: Group Properties and Elements",
        "slug": "Chapter 9: Group Properties and Elements",
        "topics": [
            "9.1 Properties of Group 1 Elements",
            "9.2 Properties of Group 17 Elements",
            "9.3 Group Properties of Transition Elements",
            "9.4 Properties of Noble Gases",
            "9.5 Physical Properties of Metals and Non-Metals"
        ]
    },
    {
        "name": "Chapter 10: Environmental Chemistry",
        "slug": "Chapter 10: Environmental Chemistry",
        "topics": [
            "10.1 Composition of Atmosphere",
            "10.2 Air Pollutants",
            "10.3 Acid Rain",
            "10.4 Global Warming (Greenhouse Effects)",
            "10.5 Strategies to Reduce Environmental Issues"
        ]
    },
    {
        "name": "Chapter 11: Hydrocarbons",
        "slug": "Chapter 11: Hydrocarbons",
        "topics": [
            "11.1 Hydrocarbons",
            "11.2 Alkanes",
            "11.3 Preparation of Alkanes",
            "11.4 Important Reactions"
        ]
    },
    {
        "name": "Chapter 12: Empirical Data Collection and Analysis",
        "slug": "Chapter 12: Empirical Data Collection and Analysis",
        "topics": [
            "12.1 SI Units in Chemistry",
            "12.2 Tools and Techniques to Manage Accuracy and Precision",
            "12.3 Accuracy and Precision"
        ]
    },
    {
        "name": "Chapter 13: Laboratory and Practical Skills",
        "slug": "Chapter 13: Laboratory and Practical Skills",
        "topics": [
            "13.1 Chemical Hazards in the Laboratory",
            "13.2 Hazard Signs",
            "13.3 Personal Protective Equipment (PPE) in the Laboratory",
            "13.4 Location of Fire Extinguisher",
            "13.5 Emergency Situations in the Lab"
        ]
    }
]
,
                10: [
  {
    "name": "Chapter 9: Chemical Equilibrium",
    "slug": "chemical-equilibrium",
    "topics": [
      "9.1 Reversible Reaction and Dynamic Equilibrium",
      "9.2 Law of Mass Action",
      "9.3 Equilibrium Constant and Its Units",
      "9.4 Importance of Equilibrium Constant"
    ]
  },
  {
    "name": "Chapter 10: Acids, Bases and Salts",
    "slug": "acids-bases-and-salts",
    "topics": [
      "10.1 Concepts of Acids and Bases",
      "10.2 pH Scale",
      "10.3 Salts"
    ]
  },
  {
    "name": "Chapter 11: Organic Chemistry",
    "slug": "organic-chemistry",
    "topics": [
      "11.1 Organic Compounds",
      "11.2 Sources of Organic Compounds",
      "11.3 Uses of Organic Compounds",
      "11.4 Alkanes and Alkyl Radicals",
      "11.5 Functional Groups",
      "11.6 Tests of Functional Groups"
    ]
  },
  {
    "name": "Chapter 12: Hydrocarbons",
    "slug": "hydrocarbons",
    "topics": [
      "12.1 Alkanes",
      "12.2 Alkenes",
      "12.3 Alkynes"
    ]
  },
  {
    "name": "Chapter 13: Biochemistry",
    "slug": "biochemistry",
    "topics": [
      "13.1 Carbohydrates",
      "13.2 Protein",
      "13.3 Lipids",
      "13.4 Nucleic Acids",
      "13.5 Vitamins"
    ]
  },
  {
    "name": "Chapter 14: Environmental Chemistry I – The Atmosphere",
    "slug": "environmental-chemistry-atmosphere",
    "topics": [
      "14.1 Composition of Atmosphere",
      "14.2 Layers of Atmosphere",
      "14.3 Pollutants",
      "14.4 Acid Rain and Its Effects",
      "14.5 Ozone Depletion and Its Effect"
    ]
  },
  {
    "name": "Chapter 15: Water",
    "slug": "water",
    "topics": [
      "15.1 Properties of Water",
      "15.2 Water as Solvent",
      "15.3 Soft and Hard Water",
      "15.4 Water Pollution",
      "15.5 Waterborne Infectious Diseases"
    ]
  },
  {
    "name": "Chapter 16: Chemical Industries",
    "slug": "chemical-industries",
    "topics": [
      "16.1 Basic Metallurgical Operations",
      "16.2 Manufacture of Sodium Carbonate by Solvay’s Process",
      "16.3 Manufacture of Urea",
      "16.4 Petroleum Industry"
    ]
  }
]
,
                11: [
    {
        "name": "Chapter 1: Periodic Table and Periodic Properties",
        "slug": "Chapter 1: Periodic Table and Periodic Properties",
        "topics": [
            "1.1 Historical Background",
            "1.2 Modern Periodic Table - Features and Significance",
            "1.3 Metals, Non-Metals and Metalloids",
            "1.4 Blocks in Periodic Table",
            "1.5 Families in Periodic Table",
            "1.6 Periodic Arrangement and Electronic Configuration",
            "1.7 Periodicity of Properties",
            "1.8 Reactions of Na and Mg with Water, Oxygen, and Chlorine",
            "1.9 Trends in Bonding in Oxides and Chlorides of Period 3",
            "1.10 Variation in Oxidation Number in Oxides and Chlorides"
        ]
    },
    {
        "name": "Chapter 2: Atomic Structure",
        "slug": "Chapter 2: Atomic Structure",
        "topics": [
            "2.1 Atomic Number, Proton Number and Nucleon Number; Identity of an Element",
            "2.2 Effect of Electric Field on Fundamental Particles",
            "2.3 Experimental Evidences for the Electronic Configuration",
            "2.4 Atomic Spectra",
            "2.5 Quantum Numbers",
            "2.6 Shapes of Atomic Orbitals",
            "2.7 Electronic Configuration",
            "2.8 Electronic Configuration and the Periodic Table",
            "2.9 Electronic Configuration of Ions and Free Radicals",
            "2.10 Electronic Configuration and the Formation of Semiconductors"
        ]
    },
    {
        "name": "Chapter 3: Chemical Bonding",
        "slug": "Chapter 3: Chemical Bonding",
        "topics": [
            "3.1 Lewis Concept of Bonding",
            "3.2 Electronegativity and the Type of Bond",
            "3.3 Covalent Bonding",
            "3.4 Electronegativity and the Type of Bond",
            "3.5 Atomic Orbital Hybridization and Shapes of Molecules",
            "3.6 Shapes of Molecules (VSEPR)",
            "3.7 Molecular Orbital Theory (MOT)",
            "3.8 Intermolecular Forces",
            "3.9 Bond Energy and Bond Length",
            "3.10 A Comparison among Ionic, Covalent, Metallic Bonds and Intermolecular Forces"
        ]
    },
    {
        "name": "Chapter 4: Stoichiometry",
        "slug": "Chapter 4: Stoichiometry",
        "topics": [
            "4.1 Concept of Mole",
            "4.2 Relationship between Mole, Molar Mass and Avogadro's Number",
            "4.3 Molar Volume",
            "4.4 Molar Mass and Density of Gases",
            "4.5 Molar Concentration",
            "4.6 Stoichiometry",
            "4.7 Limiting and Excess Reactant",
            "4.8 Theoretical Yield, Actual Yield, and Percentage Yield",
            "4.9 Importance of Stoichiometry in Production and Dosage of Medicine"
        ]
    },
    {
        "name": "Chapter 5: Phases of Matter",
        "slug": "Chapter 5: Phases of Matter",
        "topics": [
            "5.1 Properties of Gases",
            "5.2 Ideal Gas Equation",
            "5.3 Properties of Liquids",
            "5.4 Intermolecular Forces",
            "5.5 Surface Tension of Liquids",
            "5.6 Viscosity of Liquids",
            "5.7 Evaporation",
            "5.8 Vapour Pressure",
            "5.9 Boiling Point",
            "5.10 Energetic of Phase Changes",
            "5.11 General Properties of Solids",
            "5.12 Types of Solids",
            "5.13 Liquid Crystals"
        ]
    },
    {
        "name": "Chapter 6: Chemical Energetics",
        "slug": "Chapter 6: Chemical Energetics",
        "topics": [
            "6.1 Enthalpy Change",
            "6.2 Energy Profile Diagram",
            "6.3 Standard Enthalpy Changes",
            "6.4 Bond Energy (Bond Dissociation Energy) and Enthalpy Changes",
            "6.5 Enthalpy Change of Reaction (ΔHr) and Chemical Bonds",
            "6.6 Measurement of Enthalpy Change of a Reaction",
            "6.7 Enthalpy Change and Calorie Content of Food",
            "6.8 Hess' Law of Heat Summation",
            "6.9 Energetics of Solution",
            "6.10 Born-Haber Cycle",
            "6.11 Entropy",
            "6.12 Free Energy (G)"
        ]
    },
    {
        "name": "Chapter 7: Reaction Kinetics",
        "slug": "Chapter 7: Reaction Kinetics",
        "topics": [
            "7.1 Collision Theory",
            "7.2 Rate of Reaction",
            "7.3 Factors Affecting Rate of a Chemical Reaction",
            "7.4 Rate Law, Rate Constant and Order of Reaction",
            "7.5 Determination of Rate Constant",
            "7.6 Reaction Mechanism"
        ]
    },
    {
        "name": "Chapter 8: Chemical Equilibrium",
        "slug": "Chapter 8: Chemical Equilibrium",
        "topics": [
            "8.1 Macroscopic Events and Microscopic Events",
            "8.2 Reversible Reactions, Microscopic Events and Dynamic Equilibrium",
            "8.3 Relation between Macroscopic and Microscopic Events",
            "8.4 Dynamic Equilibrium between Two Physical States",
            "8.5 Conditions for Equilibrium",
            "8.6 Characteristics of Chemical Equilibrium",
            "8.7 Types of Equilibrium",
            "8.8 Equilibrium Constant and Position of Equilibrium",
            "8.9 Relationships between Various Equilibrium Constants",
            "8.10 Position of Equilibrium and Reaction Conditions",
            "8.11 Le-Chatelier's Principle",
            "8.12 The Effect of Change of Concentrations",
            "8.13 The Effect of Change in Pressure or Volume",
            "8.14 The Effect of Change in Temperature",
            "8.15 Effect of Catalyst on Equilibrium",
            "8.16 Industrial Applications of Chemical Equilibrium"
        ]
    },
    {
        "name": "Chapter 9: Acid-Base Chemistry",
        "slug": "Chapter 9: Acid-Base Chemistry",
        "topics": [
            "9.1 Bronsted-Lowry Concept",
            "9.2 Lewis Concept of Acids and Bases",
            "9.3 Ionic Product of Water",
            "9.4 pH and pOH",
            "9.5 Ionization Constants of Acids (Ka)",
            "9.6 Common Ion Effect",
            "9.7 Buffer Solutions",
            "9.8 Solubility Product",
            "9.9 Salt Hydrolysis",
            "9.10 Acid-Base Indicators"
        ]
    },
    {
        "name": "Chapter 10: Electrochemistry",
        "slug": "Chapter 10: Electrochemistry",
        "topics": [
            "10.1 Oxidation, Reduction, and Redox Reactions",
            "10.2 Oxidation Number and Its Significance",
            "10.3 Disproportionation Reaction",
            "10.4 Oxidizing Agent (Oxidant) and Reducing Agent (Reductant)",
            "10.5 Balancing of Redox Equations by Oxidation Number Method",
            "10.6 Electrolytic Cell",
            "10.7 Redox Reactions in Electrolysis",
            "10.8 Mass of a Substance Deposited During Electrolysis",
            "10.9 Amount of Substance Produced During Electrolysis",
            "10.10 Avogadro's Constant by the Electrolytic Method",
            "10.11 Electrode Potentials",
            "10.12 Standard Hydrogen Electrode",
            "10.13 Standard Electrode Potential",
            "10.14 Measuring Standard Electrode Potentials",
            "10.15 Electrochemical Cell (Galvanic Cell)",
            "10.16 Calculation of Standard Potential (E° Cell)",
            "10.17 Applications of E° Values",
            "10.18 Variation of E° Value with Ion Concentration",
            "10.19 Nernst Equation",
            "10.20 Activity Series of Metals and Ease of Oxidation",
            "10.21 Feasibility of Redox Reactions from Activity Series or Reaction Data",
            "10.22 Photovoltaic Cells",
            "10.23 Winkler Method, BOD and DO"
        ]
    },
    {
        "name": "Chapter 11: Hydrocarbons",
        "slug": "Chapter 11: Hydrocarbons",
        "topics": [
            "11.1 Aliphatic and Aromatic Hydrocarbons",
            "11.2 Nomenclature",
            "11.3 Reaction Mechanism and Modes of Bond Breaking",
            "11.4 Unreactive Nature of Alkanes Towards Polar Reagents",
            "11.5 Reactions of Alkanes",
            "11.6 Alkenes",
            "11.7 Structure and Reactivity of Alkenes",
            "11.8 Reactions of Alkenes",
            "11.9 Conjugated Dienes",
            "11.10 Isomerism",
            "11.11 Organic Redox Reactions"
        ]
    },
    {
        "name": "Chapter 12: Nitrogen and Sulfur",
        "slug": "Chapter 12: Nitrogen and Sulfur",
        "topics": [
            "12.1 Reactivity of Nitrogen (N2)",
            "12.2 Ammonia (NH3)",
            "12.3 Oxides of Nitrogen",
            "12.4 Sources of Oxides of Nitrogen",
            "12.5 Role of NO & NO2 in Smog & PAN Formation",
            "12.6 Catalytic Converter",
            "12.7 Nitrification and Denitrification",
            "12.8 Sulfur",
            "12.9 Stability of Oxidation States of Sulfur",
            "12.10 Reactions of Sulfur",
            "12.11 Uses of Sulfur and Its Compounds",
            "12.12 Role of Sulfur in Organic Synthesis of Drugs, Dyes and Fragrances",
            "12.13 Sulfuric Acid (H2SO4)"
        ]
    },
    {
        "name": "Chapter 13: Halogens",
        "slug": "Chapter 13: Halogens",
        "topics": [
            "13.1 Volatility of Chlorine, Bromine and Iodine",
            "13.2 Trend in Volatility of the Halogens",
            "13.3 The Bond Strength of Halogen Molecules",
            "13.4 Relative Reactivities of the Halogens as Oxidizing Agents",
            "13.5 Reactions of the Halogens with Hydrogen",
            "13.6 Relative Thermal Stabilities of Hydrogen Halides in Terms of Their Bond Strength",
            "13.7 Relative Reactivity of Halide Ions as Reducing Agents",
            "13.8 Reactions of Halides with Aqueous Silver Ion Followed by Aqueous Ammonia",
            "13.9 Reactions of Halides (X-) with Concentrated Sulfuric Acid",
            "13.10 Reactions of Chlorine with Cold and Hot Aqueous Sodium Hydroxide",
            "13.11 Use of Chlorine in Water Purification"
        ]
    },
    {
        "name": "Chapter 14: Atmosphere",
        "slug": "Chapter 14: Atmosphere",
        "topics": [
            "14.1 Layers of the Atmosphere",
            "14.2 Air Pollutants",
            "14.3 Sources of Air Pollution",
            "14.4 Sources of Air Pollutants",
            "14.5 Impact of Human Activities on the Atmosphere",
            "14.6 Effects of Air Pollutants",
            "14.7 Greenhouse Effect and Global Warming",
            "14.8 Air Quality",
            "14.9 Link Between Air Quality and Human Health",
            "14.10 Potential Health Risk Associated with Air Pollution",
            "14.11 Methods & Techniques to Measure & Monitor Air Quality",
            "14.12 Experiments and Data Collection to Test Hypothesis About Air Quality",
            "14.13 Analyze Data and Interpret Air Quality",
            "14.14 Strategies Used to Reduce Air Pollution",
            "14.15 Laws and Regulations Related to Atmosphere",
            "14.16 Economic, Social & Political Issues"
        ]
    },
    {
        "name": "Chapter 15: Basic Separation Techniques",
        "slug": "Chapter 15: Basic Separation Techniques",
        "topics": [
            "15.1 Methods of Separation of Mixtures",
            "15.2 Separation Through Distillation",
            "15.3 Chromatography",
            "15.4 How to Check the Purity of the Product?"
        ]
    },
    {
        "name": "Chapter 16: Lab Safety and Practical Skills",
        "slug": "Chapter 16: Lab Safety and Practical Skills",
        "topics": [
            "16.1 General Instructions to the Students",
            "16.2 Common Types of Hazards in a Laboratory",
            "16.3 Waste Disposal System for Chemicals",
            "16.4 First Aid in Laboratory",
            "16.5 Acid-Base Titration",
            "16.6 Tests for Identification of Anions",
            "16.7 Tests for Identification of Basic Radicals"
        ]
    }
]

                ,
                12:  [ 
    {
        "name": "Chapter 1: Periodic Classification of Elements and Periodicity",
        "slug": "Chapter 1: Periodic Classification of Elements and Periodicity",
        "topics": [
            "1.1 Introduction",
            "1.2 The Modern Periodic Table",
            "1.3 Periodic Trends In Physical Properties",
            "1.4 Periodic Relationship In Compounds",
            "1.5 The Position Of Hydrogen"
        ]
    },
    {
        "name": "Chapter 2: s-Block Elements",
        "slug": "Chapter 2: s-Block Elements",
        "topics": [
            "2.1 Introduction",
            "2.2 Electronic Configurations of s-Block Elements",
            "2.3 Commercial Preparation of Sodium by Downs Cell",
            "2.4 Commercial Preparation of Sodium Hydroxide by the Diaphragm Cell",
            "2.5 Role of Gypsum in Agriculture and Industry",
            "2.6 Role of Lime in Agriculture and Industry"
        ]
    },
    {
        "name": "Chapter 3: Group IIIA and Group IVA Elements",
        "slug": "Chapter 3: Group IIIA and Group IVA Elements",
        "topics": [
            "3.1 Group IIIA Elements",
            "3.2 Compounds of Boron",
            "3.3 Reactions of Aluminium",
            "3.4 Group IVA Elements",
            "3.5 Compounds of Carbon and Silicon",
            "3.6 Semiconductors",
            "3.7 Uses of Lead Compounds in Paints"
        ]
    },
    {
        "name": "Chapter 4: Group VA and Group VIA Elements",
        "slug": "Chapter 4: Group VA and Group VIA Elements",
        "topics": [
            "4.1 Introduction",
            "4.2 Nitrogen and Its Compounds",
            "4.3 Phosphorus and Its Compounds",
            "4.4 Group VIA Elements",
            "4.5 Sulphuric Acid (H2SO4) - The Manufacture, Properties, and Uses"
        ]
    },
    {
        "name": "Chapter 5: The Halogens and the Noble Gases",
        "slug": "Chapter 5: The Halogens and the Noble Gases",
        "topics": [
            "5.1 Introduction",
            "5.2 Occurrence",
            "5.3 Peculiar Behaviour of Fluorine",
            "5.4 Oxidizing Properties",
            "5.5 Compounds of Halogens",
            "5.6 Commercial Uses of Halogens and Their Compounds",
            "5.7 Noble Gases"
        ]
    },
    {
        "name": "Chapter 6: Transition Elements",
        "slug": "Chapter 6: Transition Elements",
        "topics": [
            "6.1 Introduction",
            "6.2 Properties of Transition Elements",
            "6.3 Complex Compounds",
            "6.4 Iron",
            "6.5 Corrosion",
            "6.6 Chromates and Dichromates",
            "6.7 Potassium Permanganate (KMnO4)"
        ]
    },
    {
        "name": "Chapter 7: Fundamental Principles of Organic Chemistry",
        "slug": "Chapter 7: Fundamental Principles of Organic Chemistry",
        "topics": [
            "7.1 Introduction",
            "7.2 Some Features of Organic Compounds",
            "7.3 Importance of Organic Chemistry",
            "7.4 Sources of Organic Compounds",
            "7.5 Cracking of Petroleum",
            "7.6 Reforming",
            "7.7 Classifications of Organic Compounds",
            "7.8 Functional Group"
        ]
    },
    {
        "name": "Chapter 8: Aliphatic Hydrocarbons",
        "slug": "Chapter 8: Aliphatic Hydrocarbons",
        "topics": [
            "8.1 Introduction",
            "8.2 Nomenclature",
            "8.3 Alkanes or Paraffins",
            "8.4 Alkenes",
            "8.5 Alkynes"
        ]
    },
    {
        "name": "Chapter 9: Aromatic Hydrocarbons",
        "slug": "Chapter 9: Aromatic Hydrocarbons",
        "topics": [
            "9.1 Introduction",
            "9.2 Nomenclature",
            "9.3 Benzene",
            "9.4 Preparation of Benzene",
            "9.5 Reactions of Benzene",
            "9.6 Comparison of Reactivities of Alkanes, Alkenes and Benzene"
        ]
    },
    {
        "name": "Chapter 10: Alkyl Halides",
        "slug": "Chapter 10: Alkyl Halides",
        "topics": [
            "10.1 Introduction",
            "10.2 Nomenclature of Alkyl Halides",
            "10.3 Methods of Preparation of Alkyl Halides",
            "10.4 Reactivity of Alkyl Halides",
            "10.5 Reactions of Alkyl Halides",
            "10.6 Grignard Reagent"
        ]
    },
    {
        "name": "Chapter 11: Biochemistry",
        "slug": "Chapter 11: Biochemistry",
        "topics": [
            "11.1 Introduction",
            "11.2 Alcohols",
            "11.3 Distinction Between Primary, Secondary and Tertiary Alcohols",
            "11.4 Uses of Alcohols",
            "11.5 Phenol",
            "11.6 Ethers"
        ]
    },
    {
        "name": "Chapter 12: Aldehydes and Ketones",
        "slug": "Chapter 12: Aldehydes and Ketones",
        "topics": [
            "12.1 Introduction",
            "12.2 Nomenclature",
            "12.3 Preparation of Aldehydes and Ketones",
            "12.4 Reactivity of Carbonyl Group",
            "12.5 Reactions of Carbonyl Compounds",
            "12.6 Identification of Carbonyl Compounds",
            "12.7 Uses"
        ]
    },
    {
        "name": "Chapter 13: Carboxylic Acids",
        "slug": "Chapter 13: Carboxylic Acids",
        "topics": [
            "13.1 Introduction",
            "13.2 Nomenclature of Carboxylic Acids",
            "13.3 General Methods of Preparation",
            "13.4 Physical Characteristics",
            "13.5 Reactivity of Carboxyl Group ( -C=O -OH)",
            "13.6 Reactions of Carboxylic Acids",
            "13.7 Acetic Acid",
            "13.8 Amino Acids"
        ]
    },
    {
        "name": "Chapter 14: Macromolecules",
        "slug": "Chapter 14: Macromolecules",
        "topics": [
            "14.1 Introduction",
            "14.2 Structure of Polymers",
            "14.3 Types of Polymers",
            "14.4 Polymerization Process",
            "14.5 Brief Description of Synthetic Polymers",
            "14.6 Biopolymers"
        ]
    },
    {
        "name": "Chapter 15: Common Chemical Industries in Pakistan",
        "slug": "Chapter 15: Common Chemical Industries in Pakistan",
        "topics": [
            "15.1 Introduction",
            "15.2 Fertilizers",
            "15.3 Elements Essential for Plant Growth",
            "15.4 Classification of Fertilizers",
            "15.5 Cement",
            "15.6 Paper Industry"
        ]
    },
    {
        "name": "Chapter 16: Environmental Chemistry",
        "slug": "Chapter 16: Environmental Chemistry",
        "topics": [
            "16.1 Introduction",
            "16.2 Types of Pollution",
            "16.3 Factors Affecting the Quality of Water",
            "16.4 Solid Waste Management"
        ]
    }
]

            },
            'pak_studies': {
                9: [
                    {
                        'name': 'Chapter 1: The Science Of Biology',
                        'slug': 'Chapter 1: The Science Of Biology',
                        'topics': [
                            '1.1 Biology and its Branches',
                            '1.2 Relation of Biology with Other Sciences',
                            '1.3 Careers in Biology',
                            '1.4 Quranic Instructions to Reveal the Study of Life',
                            '1.5 Science as a Collaborative Feild',
                            '1.6 Scientific Method',
                            '1.7 Theory and Law/Principle',
                            '1.8 Malaria -An Example of Biological Method',
                        ]
                    },
                    {
                        'name': 'Chapter 2: Biodiversity',
                        'slug': 'matChapter 2: Biodiversityter',
                        'topics': [
                            '2.1 Biodiversity',
                            '2.2 Classification',
                            '2.3 Taxonomic Ranks',
                            '2.4 History of Classification',
                            '2.5 Domains of Living Organisms',
                            '2.6 Classification of Domain Eukarya',
                            '2.7 Status of Virus in Classification',
                            '2.8 Bionomial Nomenclature'
                        ]
                    },
                    {
                        'name': 'Chapter 3: The Cell',
                        'slug': 'Chapter 3: The Cell',
                        'topics': [
                            '3.1 Cell',
                            '3.2 Structure of Cell',
                            '3.3 Structural Advantages of Plant and Animal Cells',
                            '3.4 Cell Specilization',
                            '3.5 Stem Cells',
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 4: Cell Cycle',
                        'slug': 'Chapter 4: Cell Cycle',
                        'topics': [
                            '4.1 Cell Cycle',
                            '4.2 Mitosis',
                            '4.3 Meiosis',
                            '4.4 Comparison between Mitosis and Meiosis',
                        ]
                    },
                    {
                        'name': 'Chapter 5: Tissues, Organs, and Organ Systems',
                        'slug': 'Chapter 5: Tissues, Organs, and Organ Systems',
                        'topics': [
                            '5.1 Levels of Organization',
                            '5.2 Organs and Organ Systems in Plants ',
                            '5.3 Organs and Organ Systems in Humans',
                            '5.4 Homeostatis'
                        ]
                    },
                    {
                        'name': 'Chapter 6: Biomolecules',
                        'slug': 'Chapter 6: Biomolecules',
                        'topics': [
                            '6.1 Biomolecules',
                            '6.2 Carbohydrates',
                            '6.3 Proteins',
                            '6.4 Lipids',
                            '6.5 Nucleic Acids',
                            '6.6 The Working of DNA and RNA'
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 7: Enzymes',
                        'slug': 'Chapter 7: Enzymes',
                        'topics': [
                            '7.1 Metabolism',
                            '7.2 Enzymes',
                            '7.3 Mechanism of Enzyme Action',
                            '7.4 Factors that Affect the Activity of Enzymes',
                            '7.5 Enzyme Inhibition'
                        ]
                    },
                    {
                        'name': 'Chapter 8: Bioenergetics',
                        'slug': 'Chapter 8: Bioenergetics',
                        'topics': [
                            '8.1 ATP: The Cell\'s Energy Currency',
                            '8.2 Photosynthesis',
                            '8.3 Cellular Respiration',
                            
                        ]
                    },
                    {
                        'name': 'Chapter 9: Plant Physiology',
                        'slug': 'Chapter 9: Plant Physiology',
                        'topics': [
                            '9.1 Nutrition in Plants',
                            '9.2 Transport in Plants',
                            '9.3 Transpiration',
                            '9.4 Transport of Water and Salt in Plants',
                            '9.5 Translocation of Food in Plant',
                            '9.6 Gaseous Exchange in Plants',
                            '9.7 Mechanisms for Excretion in Plants',
                            '9.8 Osmotic Adjustments in Plants'
                        ]
                    },
                    {
                        'name': 'Chapter 10: Respiration in Plants',
                        'slug': 'Chapter 10: Respiration in Plants',
                        'topics': [
                            '10.1 Types of Asexual Reproduction',
                            '10.2  Artificial Propagation',
                            '10.3 Sexual Reproduction in Plants',
                            
                        ]
                    },
                    {
                        'name': 'Chapter 11: Biostatistics',
                        'slug': 'Chapter 11: Biostatistics',
                        'topics': [
                            '11.1 Introduction of Biostatistics',
                            '11.2 Mean, Median,and Mode',
                            '11.3 Bar Chart'                        ]
                    }
                ],
                10: [
                    {
                        'name': 'Chemical Reactions',
                        'slug': 'chemical-reactions',
                        'topics': [
                            'Types of Reactions',
                            'Acids, Bases and Salts',
                            'Metals and Non-metals',
                            'Carbon Compounds'
                        ]
                    },
                    
                ],
                11: [
                    {
                        'name': 'Physical World and Measurement',
                        'slug': 'physical-world',
                        'topics': [
                            'Units and Dimensions',
                            'Errors in Measurement',
                            'Physics in Daily Life',
                            'Scientific Method'
                        ]
                    },
                    {
                        'name': 'Organic Chemistry',
                        'slug': 'organic-chemistry',
                        'topics': [
                            'Basic Organic Chemistry',
                            'Hydrocarbons',
                            'Environmental Chemistry',
                            'Polymers'
                        ]
                    }
                ],
                12: [
                    {
                        'name': 'Electromagnetic Waves',
                        'slug': 'electromagnetic-waves',
                        'topics': [
                            'Wave Optics',
                            'Electromagnetic Spectrum',
                            'Dual Nature of Matter',
                            'Quantum Physics'
                        ]
                    },
                    {
                        'name': 'Molecular Biology',
                        'slug': 'molecular-biology',
                        'topics': [
                            'DNA and RNA',
                            'Genetic Code',
                            'Evolution',
                            'Biotechnology'
                        ]
                    }
                ]
            },
            'islamiyat': {
                9: [
                    {
                        'name': 'Chapter 1: The Science Of Biology',
                        'slug': 'Chapter 1: The Science Of Biology',
                        'topics': [
                            '1.1 Biology and its Branches',
                            '1.2 Relation of Biology with Other Sciences',
                            '1.3 Careers in Biology',
                            '1.4 Quranic Instructions to Reveal the Study of Life',
                            '1.5 Science as a Collaborative Feild',
                            '1.6 Scientific Method',
                            '1.7 Theory and Law/Principle',
                            '1.8 Malaria -An Example of Biological Method',
                        ]
                    },
                    {
                        'name': 'Chapter 2: Biodiversity',
                        'slug': 'matChapter 2: Biodiversityter',
                        'topics': [
                            '2.1 Biodiversity',
                            '2.2 Classification',
                            '2.3 Taxonomic Ranks',
                            '2.4 History of Classification',
                            '2.5 Domains of Living Organisms',
                            '2.6 Classification of Domain Eukarya',
                            '2.7 Status of Virus in Classification',
                            '2.8 Bionomial Nomenclature'
                        ]
                    },
                    {
                        'name': 'Chapter 3: The Cell',
                        'slug': 'Chapter 3: The Cell',
                        'topics': [
                            '3.1 Cell',
                            '3.2 Structure of Cell',
                            '3.3 Structural Advantages of Plant and Animal Cells',
                            '3.4 Cell Specilization',
                            '3.5 Stem Cells',
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 4: Cell Cycle',
                        'slug': 'Chapter 4: Cell Cycle',
                        'topics': [
                            '4.1 Cell Cycle',
                            '4.2 Mitosis',
                            '4.3 Meiosis',
                            '4.4 Comparison between Mitosis and Meiosis',
                        ]
                    },
                    {
                        'name': 'Chapter 5: Tissues, Organs, and Organ Systems',
                        'slug': 'Chapter 5: Tissues, Organs, and Organ Systems',
                        'topics': [
                            '5.1 Levels of Organization',
                            '5.2 Organs and Organ Systems in Plants ',
                            '5.3 Organs and Organ Systems in Humans',
                            '5.4 Homeostatis'
                        ]
                    },
                    {
                        'name': 'Chapter 6: Biomolecules',
                        'slug': 'Chapter 6: Biomolecules',
                        'topics': [
                            '6.1 Biomolecules',
                            '6.2 Carbohydrates',
                            '6.3 Proteins',
                            '6.4 Lipids',
                            '6.5 Nucleic Acids',
                            '6.6 The Working of DNA and RNA'
                        ]
                    }
                    ,
                    {
                        'name': 'Chapter 7: Enzymes',
                        'slug': 'Chapter 7: Enzymes',
                        'topics': [
                            '7.1 Metabolism',
                            '7.2 Enzymes',
                            '7.3 Mechanism of Enzyme Action',
                            '7.4 Factors that Affect the Activity of Enzymes',
                            '7.5 Enzyme Inhibition'
                        ]
                    },
                    {
                        'name': 'Chapter 8: Bioenergetics',
                        'slug': 'Chapter 8: Bioenergetics',
                        'topics': [
                            '8.1 ATP: The Cell\'s Energy Currency',
                            '8.2 Photosynthesis',
                            '8.3 Cellular Respiration',
                            
                        ]
                    },
                    {
                        'name': 'Chapter 9: Plant Physiology',
                        'slug': 'Chapter 9: Plant Physiology',
                        'topics': [
                            '9.1 Nutrition in Plants',
                            '9.2 Transport in Plants',
                            '9.3 Transpiration',
                            '9.4 Transport of Water and Salt in Plants',
                            '9.5 Translocation of Food in Plant',
                            '9.6 Gaseous Exchange in Plants',
                            '9.7 Mechanisms for Excretion in Plants',
                            '9.8 Osmotic Adjustments in Plants'
                        ]
                    },
                    {
                        'name': 'Chapter 10: Respiration in Plants',
                        'slug': 'Chapter 10: Respiration in Plants',
                        'topics': [
                            '10.1 Types of Asexual Reproduction',
                            '10.2  Artificial Propagation',
                            '10.3 Sexual Reproduction in Plants',
                            
                        ]
                    },
                    {
                        'name': 'Chapter 11: Biostatistics',
                        'slug': 'Chapter 11: Biostatistics',
                        'topics': [
                            '11.1 Introduction of Biostatistics',
                            '11.2 Mean, Median,and Mode',
                            '11.3 Bar Chart'                        ]
                    }
                ],
                10: [
                    {
                        'name': 'Chemical Reactions',
                        'slug': 'chemical-reactions',
                        'topics': [
                            'Types of Reactions',
                            'Acids, Bases and Salts',
                            'Metals and Non-metals',
                            'Carbon Compounds'
                        ]
                    },
                    
                ],
                11: [
                    {
                        'name': 'Physical World and Measurement',
                        'slug': 'physical-world',
                        'topics': [
                            'Units and Dimensions',
                            'Errors in Measurement',
                            'Physics in Daily Life',
                            'Scientific Method'
                        ]
                    },
                    {
                        'name': 'Organic Chemistry',
                        'slug': 'organic-chemistry',
                        'topics': [
                            'Basic Organic Chemistry',
                            'Hydrocarbons',
                            'Environmental Chemistry',
                            'Polymers'
                        ]
                    }
                ],
                12: [
                    {
                        'name': 'Electromagnetic Waves',
                        'slug': 'electromagnetic-waves',
                        'topics': [
                            'Wave Optics',
                            'Electromagnetic Spectrum',
                            'Dual Nature of Matter',
                            'Quantum Physics'
                        ]
                    },
                    {
                        'name': 'Molecular Biology',
                        'slug': 'molecular-biology',
                        'topics': [
                            'DNA and RNA',
                            'Genetic Code',
                            'Evolution',
                            'Biotechnology'
                        ]
                    }
                ]
            }
            
        }
    }

