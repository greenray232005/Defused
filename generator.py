import csv
import os

with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name, age, gender, hobby1, hobby2, personality, location = row
        profile_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="styles.css">
        </head>
        <body>
            <header>
                <h1 class="web-name">Connec</h1>
            </header>
            <div class="profile-card">
                <img class="profile-pic" src="https://robohash.org/{name.replace(' ', '%20')}.png" alt="Profile Picture">
                <h2 class="profile-name">{name}</h2>
                <div class="profile-info-grid">
                    <div class="info-item">
                        <h3>Age</h3>
                        <p>{age}</p>
                    </div>
                    <div class="info-item">
                        <h3>Gender</h3>
                        <p>{gender}</p>
                    </div>
                    <div class="info-item">
                        <h3>Hobbies</h3>
                        <p>{hobby1}, {hobby2}</p>
                    </div>
                    <div class="info-item">
                        <h3>Personality</h3>
                        <p>{personality}</p>
                    </div>
                    <div class="info-item">
                        <h3>Location</h3>
                        <p>{location}</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        with open(f'{name.replace(" ", "_")}_profile.html', 'w') as profile_file:
            profile_file.write(profile_html)