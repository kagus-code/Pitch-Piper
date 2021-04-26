import unittest
from app.models import Pitch,User
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()


    def setUp(self):
    self.user_kagus = User(
        username='kagus', password='pass', email='james@ms.com')
    self.new_pitch = Pitch(pitch_title='testing', pitch_post='this is the pitch', pitch_category="Production",
                              posted='12/8/2021', user=self.user_kagus)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,'testing')
        self.assertEquals(self.new_pitch.pitch_post,'this is the pitch')
        self.assertEquals(self.new_pitch.pitch_category,"Production")
        self.assertEquals(self.new_pitch.posted,'12/8/2021')
        self.assertEquals(self.new_pitch.user, self.user_kagus)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)
   