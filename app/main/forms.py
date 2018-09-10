from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators = [Required()])
    body = TextAreaField('Your Pitch', validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Review or Comments', validators = [Required()])
    submit = SubmitField('Submit')


class VoteForm(FlaskForm):
    rating = RadioField('Do you like this Pitch? Upvote or Downvote it',
                        choices=[('upvote', 'upvote'),
                                 ('downvote', 'downvote')],
                        validators=[Required()])


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself.',
                        validators=[Required()])