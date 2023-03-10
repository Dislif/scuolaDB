"""added table materie

Revision ID: 4832d47e8aba
Revises: 2ed15fc3bb9e
Create Date: 2023-02-05 15:24:31.182112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4832d47e8aba'
down_revision = '2ed15fc3bb9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=True),
    sa.Column('classe_concorso', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('materie')
    # ### end Alembic commands ###
