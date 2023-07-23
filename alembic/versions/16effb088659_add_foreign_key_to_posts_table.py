"""add foreign-key to posts table

Revision ID: 16effb088659
Revises: b4f8e5ed0aac
Create Date: 2023-07-23 11:25:15.629309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16effb088659'
down_revision = 'b4f8e5ed0aac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
