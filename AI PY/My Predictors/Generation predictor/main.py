# Inserting all the datasets

import json

gen_json = '''
    {
        "Generations": [
            {
                "name": "Silent Generation",
                "start_year": 1926,
                "end_year": 1945,
                "tech": [
                    "Radio",
                    "Typewriter",
                    "black_and_white_television",
                    "vinyl_records",
                    "Telephone",
                    "Telegraph",
                    "Film_projector",
                    "Gramophone",
                    "Newspaper"
                ],
                "people": [
                    "Franklin D. Roosevelt",
                    "Winston Churchill",
                    "Albert Einstein",
                    "Marilyn Monroe",
                    "John Wayne",
                    "Frank Sinatra",
                    "Mahatma Gandhi",
                    "Jawaharlal Nehru",
                    "Adolf Hitler",
                    "Joseph Stalin",
                    "Charlie Chaplin",
                    "Nelson Mandela",
                    "Mother Teresa",
                    "Hideki Tojo",
                    "Dwight D. Eisenhower",
                    "Theodore Roosevelt",
                    "Anne Frank"
                ],
                "events": [
                    "Great Depression",
                    "World War II",
                    "Korean War",
                    "Indian Independence",
                    "Chinese Civil War",
                    "Formation of the United Nations",
                    "Partition of India",
                    "Beginning of the Cold War"
                ]
            },
            {
                "name": "Baby Boomers",
                "start_year": 1946,
                "end_year": 1964,
                "tech": [
                    "Telephone",
                    "Newspaper",
                    "Radio",
                    "Color_television",
                    "Cassette"
                ],
                "people": [
                    "Elvis Presley",
                    "John F. Kennedy",
                    "Marilyn Monroe",
                    "Martin Luther King Jr.",
                    "The Beatles",
                    "Muhammad Ali",
                    "Pele",
                    "Queen",
                    "Michael Jackson",
                    "Lal Bahadur Shastri",
                    "Indira Gandhi"
                ],
                "events": [
                    "Civil Rights Movement",
                    "Vietnam War",
                    "Moon Landing",
                    "Space Race",
                    
                ]
            },
            {
                "name": "Generation X",
                "start_year": 1965,
                "end_year": 1980,
                "tech": [
                    "Personal Computer",
                    "VCR",
                    "CD",
                    "Video Games",
                    "Mobile Phones"
                ],
                "people": [
                    
                ],
                "events": [
                    "Fall of the Berlin Wall",
                    "End of the Cold War",
                    "Rise of the Internet"
                ]
            },
            {
                "name": "Millennials",
                "start_year": 1981,
                "end_year": 1996,
                "tech": [
                    
                ],
                "people": [
                    
                ],
                "events": [
                    
                ]
            },
            {
                "name": "Generation Z",
                "start_year": 1997,
                "end_year": 2012,
                "tech": [
                    
                ],
                "people": [
                    
                ],
                "events": [
                    
                ]
            },
            {
                "name": "Generation Alpha",
                "start_year": 2013,
                "end_year": 2025,
                "tech": [
                    
                ],
                "people": [
                    
                ],
                "events": [
                    
                ]
            }
        ]
    }
'''

weights = {
    "yes": 1,
    "maybe": 0.5,
    "no": -0.5,
    "don't know": -1
}