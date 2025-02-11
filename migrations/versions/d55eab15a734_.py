"""empty message

Revision ID: d55eab15a734
Revises: 
Create Date: 2020-09-24 11:57:30.501179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd55eab15a734'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('example',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('context', sa.String(), nullable=True),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer_a', sa.String(), nullable=True),
    sa.Column('answer_b', sa.String(), nullable=True),
    sa.Column('answer_c', sa.String(), nullable=True),
    sa.Column('correct_answer', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('example')
    # ### end Alembic commands ###
