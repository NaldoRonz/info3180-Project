"""empty message

Revision ID: c9174ff09bef
Revises: 5e2f882ba60d
Create Date: 2020-03-30 13:59:36.345481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9174ff09bef'
down_revision = '5e2f882ba60d'
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
