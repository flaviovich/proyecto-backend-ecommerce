"""added marcas.estado

Revision ID: 63ba2e8b4c50
Revises: 26e6b853b4bd
Create Date: 2022-10-19 17:58:35.218184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ba2e8b4c50'
down_revision = '26e6b853b4bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('marcas', sa.Column('estado', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('marcas', 'estado')
    # ### end Alembic commands ###
