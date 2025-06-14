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
            'History': {
                'description': 'Explore the events that shaped the world throughout history.',
                'anchor': 'https://www.safaracademy.com/subjects/history'
            },
            'Geography': {
                'description': 'Learn about the world’s geography, maps, and earth sciences.',
                'anchor': 'https://www.safaracademy.com/subjects/geography'
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
            'computer': {
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

