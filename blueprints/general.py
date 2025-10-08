from flask import Blueprint , render_template , abort
import json
from models.story import Story ,StoryPart
from models.character import Character


app = Blueprint('general' , __name__)


@app.route("/")
def main ():
    stories = Story.query.all()
    characters = Character.query.all()
    return render_template("main.html" , stories = stories , characters = characters)


@app.route("/stories")
def story_list():
    stories = Story.query.all()
    return render_template("story_list.html" , stories = stories)

@app.route("/story/<slug>")
def story_detail(slug):
    story = Story.query.filter_by(slug = slug).first_or_404()
    return render_template("story_detail.html" , story = story)


@app.route("/story/<slug>/part/<int:part_id>")
def story_part(slug,part_id):
    story = Story.query.filter_by(slug = slug).first_or_404()
    part = StoryPart.query.get_or_404(part_id)

    if part.story_id != story.id:
        abort(404)
    
    next_part = StoryPart.query.filter(StoryPart.story_id == story.id , StoryPart.id > part.id).order_by(StoryPart.id.asc()).first()
    prev_part = StoryPart.query.filter(StoryPart.story_id == story.id , StoryPart.id < part.id).order_by(StoryPart.id.desc()).first()

    all_parts = StoryPart.query.filter_by(story_id = story.id).order_by(StoryPart.id.asc()).all()

    return render_template("story_part.html" , story = story , part = part , next_part = next_part , prev_part = prev_part , all_parts = all_parts)



@app.route("/character/<slug>")
def character_detail(slug):
    char = Character.query.filter_by(slug = slug).first_or_404()
    return render_template("character_detail.html" , char = char)