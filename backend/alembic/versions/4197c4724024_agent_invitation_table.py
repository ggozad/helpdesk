"""Agent invitation table

Revision ID: 4197c4724024
Revises: 93bca74d730f
Create Date: 2020-12-09 12:06:53.914451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4197c4724024'
down_revision = '93bca74d730f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent_invitations',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agent_invitations')
    # ### end Alembic commands ###