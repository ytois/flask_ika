"""empty message

Revision ID: 35d79da81783
Revises: 9050045bf92b
Create Date: 2017-12-08 09:28:27.597782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35d79da81783'
down_revision = '9050045bf92b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('battle_members', sa.Column('nickname', sa.String(), nullable=False))
    op.add_column('battle_members', sa.Column('player_rank', sa.Integer(), nullable=True))
    op.drop_column('battle_members', 'rank')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('battle_members', sa.Column('rank', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('battle_members', 'player_rank')
    op.drop_column('battle_members', 'nickname')
    # ### end Alembic commands ###
