# render html file with flask

from flask import Flask, render_template

app = Flask(__name__)
 
class Data:
  def __init__(self):
    self.name = " Hai Dang "
    self.age = 20
    self.address = "TPHCM, Vietnam"
    self.email = "haidangattt@gmail.com"
    self.phone = "0983785604"
  def aboutme(self):
       return f'''
        🎶🎶🎶Hello, my name is {self.name}, and I am currently a third-year student majoring
        in Information Security at the Academy of Cryptography Techniques. With a deep passion
        for cybersecurity and a commitment to learning, I have dedicated myself to mastering
        the principles and practices of information protection. Through my academic journey and 
        hands-on projects, I have gained valuable insights and skills in this ever-evolving field.
        Additionally, I actively participate in clubs and extracurricular activities to enhance my soft 
        skills and broaden my professional network. I am confident that my solid foundation in cybersecurity,
        coupled with my eagerness to learn, will enable me to make meaningful contributions to any 
        organization and the wider community in the future.🎶🎶🎶'''
  def skills(self):
    data = ["Python", "NodeJS", "Linux","Rust", "Docker", "GIT", "Tool Pentest", "Blockchain"]      
    return data
  def competitions(self):
    data = ["Vietnam Hackathon: Onchain Names & Identity", "Mamathon Hackathon","DTU CTF"]
    return data
  def projects(self):
    data = ["DWEB", "Project 2", "Project 3"]
    return data
  def experiences(self):
    data = ["Student at Academy of Cryptography Techniques, TPHCM","Intern Blockchain developers in FRIENDIFY AI Company"]
    return data
data=Data()
print(data.skills()[1])  # 

@app.route('/')
def home():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run("0.0.0.0", port = 3000)