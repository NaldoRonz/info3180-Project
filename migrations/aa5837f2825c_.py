"""empty message

Revision ID: aa5837f2825c
Revises: 
Create Date: 2020-03-29 15:10:26.056813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa5837f2825c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('my_followers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_followers',
    sa.Column('follower_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('follower_fname', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('follower_lname', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('follower_id', name='my_followers_pkey')
    )
    # ### end Alembic commands ###