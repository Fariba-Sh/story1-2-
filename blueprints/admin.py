from flask import Blueprint ,current_app, render_template , redirect , request , url_for , flash
import json , os
from models.story import Story , StoryPart
from models.character import Character
from extentions import *
import uuid

app = Blueprint('admin' , __name__ , url_prefix="/admin")


@app.route("/dashboard")
def dashboard():
    stories = Story.query.all()
    return render_template("admin/dashboard.html" , stories = stories)


@app.route("/new-story" , methods = ["POST"])
def new_story():
        title = request.form["title"]
        desc = request.form["desc"]
        slug = str(uuid.uuid4())[:8]


        story = Story(title = title , desc = desc , slug = slug)
        db.session.add(story)
        db.session.commit()
        flash("داستان اضافه شد ")
        return redirect(url_for("admin.dashboard"))
    

@app.route("/new-part/<int:story_id>" , methods = ["POST"])
def new_part(story_id):
    
        title = request.form["title"]
        content = request.form["content"]
        part = StoryPart(title = title , content = content , story_id = story_id)
        db.session.add(part)
        db. session.commit()
        
        flash("قسمت جدید اضافه شد ")
        return redirect(url_for("admin.dashboard"))
   


@app.route("/story/delete/<int:story_id>" , methods = ["POST"])
def delete_story(story_id):
       story = Story.query.get_or_404(story_id)
       db.session.delete(story)
       db.session.commit()
       flash('داستان حذف شد')
       return redirect(url_for("admin.dashboard"))



@app.route("/story/edit/<int:story_id>" , methods = ["GET" , "POST"])
def edit_story(story_id):
       story = Story.query.get_or_404(story_id)
       if request.method == "POST":
              story.title = request.form["title"]
              story.desc = request.form["desc"]
              db.session.commit()
              flash("داستان ویرایش شد ")
              return redirect(url_for("admin.dashboard"))
       return render_template("admin/edit_story.html" , story = story)




@app.route("/part/delete/<int:part_id>" , methods = ["POST"])
def delete_part(part_id):
       part = StoryPart.query.get_or_404(part_id)
       story_id = part.story_id
       db.session.delete(part)
       db.session.commit()
       flash("قسمت حذف شد")
       return redirect (url_for("admin.dashboard"))




@app.route("/part/edit/<int:part_id>" , methods = ["GET" , "POST"])
def edit_part(part_id):
       part = StoryPart.query.get_or_404(part_id)
       if request.method == "POST":
              part.title = request.form["title"]
              part.content = request.form["content"]
              db.session.commit()
              flash("قسمت ویرایش شد ")
              return redirect(url_for("admin.dashboard"))
       return render_template("admin/edit_part.html" , part = part)




@app.route('/characters')
def characters():
       chars = Character.query.all()
       return render_template("admin/characters.html" , chars = chars)



@app.route("/character/new" , methods = ["GET" , "POST"])
def new_character():
       if request.method == "POST":
              name = request.form["name"]
              desc = request.form["desc"]
              thumb = request.files["thumb"]
              full = request.files["full"]

              slug = str(uuid.uuid4())[:8]

              thumb_filename = f"{slug}_thumb.jpg"
              full_filename = f"{slug}_full.jpg"

              thumb.save(os.path.join(current_app.static_folder,"images/gallery/thumbs"  , thumb_filename))
              full.save(os.path.join(current_app.static_folder,"images/gallery/fulls" , full_filename))

              char = Character(
                     name = name,
                     desc = desc,
                     image_thumb = f"images/gallery/thumbs/{thumb_filename}",
                     image_full = f"images/gallery/fulls/{full_filename}",
                     slug = slug ,
              )

              db.session.add(char)
              db.session.commit()
              flash("شخصیت جدید اضافه شد")
              return redirect(url_for("admin.characters"))

       return render_template("admin/new_character.html")


@app.route("/character/delete/<int:char_id>" , methods =["POST"])
def delete_character(char_id):
       char = Character.query.get_or_404(char_id)
       db.session.delete(char)
       db.session.commit()
       flash("شخصیت حذف شد")
       return redirect(url_for("admin.characters"))
