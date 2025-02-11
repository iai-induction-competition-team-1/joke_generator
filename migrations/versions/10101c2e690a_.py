"""empty message

Revision ID: 10101c2e690a
Revises: 1fe4834663a0
Create Date: 2020-09-28 14:15:44.416977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10101c2e690a'
down_revision = '1fe4834663a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('new_answer_example',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seed_example_id', sa.Integer(), nullable=False),
    sa.Column('answer', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['seed_example_id'], ['seed_example.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('new_context_example',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seed_example_id', sa.Integer(), nullable=False),
    sa.Column('context', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['seed_example_id'], ['seed_example.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('new_question_example',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seed_example_id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['seed_example_id'], ['seed_example.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('new_question_example')
    op.drop_table('new_context_example')
    op.drop_table('new_answer_example')
    # ### end Alembic commands ###
