import unittest
from app.models import Comment
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()



    def setUp(self):
    self.user_kagus = User(
        username='kagus', password='pass', email='james@ms.com')
    self.new_pitch = Pitch(pitch_title='testing', pitch_post='this is the pitch', pitch_category="Production",
                              posted='12/8/2021', user=self.user_kagus,comment="great pitch")
    

    self.new_comment=Comment(comment="great pitch",user=self.user_kagus,pitch=self.new_pitch)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'testing')
        self.assertEquals(self.new_comment.user,self.user_kagus)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)