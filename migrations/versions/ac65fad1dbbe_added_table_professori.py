"""added table professori

Revision ID: ac65fad1dbbe
Revises: 410d0173cac6
Create Date: 2023-02-05 15:31:45.872276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac65fad1dbbe'
down_revision = '410d0173cac6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('professori',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classe_concorso', sa.String(length=5), nullable=True),
    sa.Column('utente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['utente_id'], ['utenti.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('professori')
    # ### end Alembic commands ###