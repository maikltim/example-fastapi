"""add last few columns to posts table

Revision ID: 048568f16320
Revises: 16effb088659
Create Date: 2023-07-23 11:31:40.433229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '048568f16320'
down_revision = '16effb088659'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text 
    ('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
