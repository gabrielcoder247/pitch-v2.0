from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

<<<<<<< HEAD
=======
class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators = [Required()])
    post = TextAreaField('Your Pitch', validators = [Required()])
    submit = SubmitField('Submit')
>>>>>>> 3e64a2d57cc9000291e11f7aa738690ca5fea512

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


class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators = [Required()])
    body = TextAreaField('Your Pitch', validators = [Required()])
    submit = SubmitField('Submit')


class InterviewForm(FlaskForm):
    title = StringField('Pitch Title', validators = [Required()])
    body = TextAreaField('Your Pitch', validators = [Required()])
    submit = SubmitField('Submit')

# class SalesForm(FlaskForm):
#     title = StringField('Pitch Title', validators = [Required()])
#     body = TextAreaField('Your Pitch', validators = [Required()])
#     submit = SubmitField('Submit')

# class InvestmentForm(FlaskForm):
#     title = StringField('Pitch Title', validators = [Required()])
#     body = TextAreaField('Your Pitch', validators = [Required()])
#     submit = SubmitField('Submit')

# class CustomerForm(FlaskForm):
#     title = StringField('Pitch Title', validators = [Required()])
#     body = TextAreaField('Your Pitch', validators = [Required()])
#     submit = SubmitField('Submit')

# class EmployeeForm(FlaskForm):
#     title = StringField('Pitch Title', validators = [Required()])
#     body = TextAreaField('Your Pitch', validators = [Required()])
#     submit = SubmitField('Submit')


# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.', validators=[Required()])
#     submit = SubmitField('Submit')


# class GeneralForm(FlaskForm):
#     post = StringField('Title', validators=[Required()])
#     body = TextAreaField('Post', validators=[Required()])
#     submit = SubmitField('Submit')
    
    
# class PitchForm(FlaskForm):
#     pitch_title = StringField('Title', validators=[Required()])
#     content = TextAreaField('Pitch', validators=[Required()])
#     category = SelectField('Category', choices=[('Advertisement','Advertisement Pitch'),('Project','Project Pitch'),('General','General Pitch'),('Sale','Sale Pitch')], validators=[Required()])
#     submit = SubmitField('Write Pitch!')

# class CommentForm(FlaskForm):
#     comment_content = TextAreaField('Write a comment', validators=[Required()])
#     submit = SubmitField('Comment')


# class GeneralReviewForm(FlaskForm):
#     review = StringField('Review: ', validators=[Required()])
#     submit = SubmitField('Submit')


# class SaleForm(FlaskForm):
#     post = StringField('Title', validators=[Required()])
#     body = TextAreaField('Post', validators=[Required()])
#     submit = SubmitField('Submit')


# class SaleReviewForm(FlaskForm):
#     review = StringField('Review: ', validators=[Required()])
#     submit = SubmitField('Submit')


# class SeductionForm(FlaskForm):
#     post = StringField('Title', validators=[Required()])
#     body = TextAreaField('Post', validators=[Required()])
#     submit = SubmitField('Submit')


# class SeductionReviewForm(FlaskForm):
#     review = StringField('Review: ', validators=[Required()])
#     submit = SubmitField('Submit')


# class MusicForm(FlaskForm):
#     post = StringField('Title', validators=[Required()])
#     body = TextAreaField('Post', validators=[Required()])
#     submit = SubmitField('Submit')


# class MusicReviewForm(FlaskForm):
#     review = StringField('Review: ', validators=[Required()])
#     submit = SubmitField('Submit')

# class ProjectForm(FlaskForm):
#     post = StringField('Title', validators=[Required()])
#     body = TextAreaField('Post', validators=[Required()])
#     submit = SubmitField('Submit')


# class ProjectReviewForm(FlaskForm):
#     review = StringField('Review: ', validators=[Required()])
#     submit = SubmitField('Submit')


# class InterviewForm(FlaskForm):
#     post = StringField('Title', validators=[Required()])
#     body = TextAreaField('Post', validators=[Required()])
#     submit = SubmitField('Submit')


# class InterviewReviewForm(FlaskForm):
#     review = StringField('Review: ', validators=[Required()])
#     submit = SubmitField('Submit')


# class AdvertisementForm(FlaskForm):
#     post = StringField('Title', validators=[Required()])
#     body = TextAreaField('Post', validators=[Required()])
#     submit = SubmitField('Submit')


# class AdvertisementReviewForm(FlaskForm):
#     review = StringField('Review: ', validators=[Required()])
#     submit = SubmitField('Submit')
