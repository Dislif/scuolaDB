"""added table voti

Revision ID: 10ce7add4f06
Revises: 8c44d73c09bb
Create Date: 2023-02-05 15:37:40.741687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10ce7add4f06'
down_revision = '8c44d73c09bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voti',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('valutazione', sa.Integer(), nullable=True),
    sa.Column('annotazione', sa.String(length=255), nullable=True),
    sa.Column('data_valutazione', sa.Date(), nullable=True),
    sa.Column('alunno_id', sa.Integer(), nullable=True),
    sa.Column('materia_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['alunno_id'], ['alunni.id'], ),
    sa.ForeignKeyConstraint(['materia_id'], ['materie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voti')
    # ### end Alembic commands ###
