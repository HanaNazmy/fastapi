"""add content column to posts table

Revision ID: f0a9548e71db
Revises: 1c3c7217ed08
Create Date: 2023-01-07 14:47:09.126985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0a9548e71db'
down_revision = '1c3c7217ed08'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
