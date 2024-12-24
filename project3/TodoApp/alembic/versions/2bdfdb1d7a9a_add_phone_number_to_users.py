"""Add phone_number to users

Revision ID: 2bdfdb1d7a9a
Revises: dec91eaeec42
Create Date: 2024-12-16 16:22:44.021375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bdfdb1d7a9a'
down_revision: Union[str, None] = 'dec91eaeec42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # op.drop_column('users', 'phone number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('users', sa.Column('phone number', sa.VARCHAR(), nullable=True))
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###