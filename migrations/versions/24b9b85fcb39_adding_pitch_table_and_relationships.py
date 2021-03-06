"""adding Pitch table and relationships

Revision ID: 24b9b85fcb39
Revises: 95b808d9884b
Create Date: 2021-04-25 22:09:57.564641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24b9b85fcb39'
down_revision = '95b808d9884b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_title', sa.String(), nullable=True),
    sa.Column('pitch_post', sa.String(), nullable=True),
    sa.Column('pitch_category', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    # ### end Alembic commands ###
