"""email in agent

Revision ID: 93bca74d730f
Revises: e0d690da188f
Create Date: 2020-12-08 10:00:19.457077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93bca74d730f'
down_revision = 'e0d690da188f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agents', sa.Column('email', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('agents', 'email')
    # ### end Alembic commands ###
