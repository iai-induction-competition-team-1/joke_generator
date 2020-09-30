"""empty message

Revision ID: 093cda9234be
Revises: 0f3f77989a1a
Create Date: 2020-09-30 11:46:50.691764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '093cda9234be'
down_revision = '0f3f77989a1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('new_answer_example_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['new_answer_example_id'], ['new_answer_example.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    # ### end Alembic commands ###
