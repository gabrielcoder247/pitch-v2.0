"""add to db schema

Revision ID: 1f187e6edc42
Revises: 2e9c67f30e8d
Create Date: 2018-09-10 20:32:49.088306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f187e6edc42'
down_revision = '2e9c67f30e8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('categories', sa.Column('name_', sa.String(length=255), nullable=True))
    op.drop_column('categories', 'category_description')
    op.drop_column('categories', 'name_of_category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('name_of_category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('categories', sa.Column('category_description', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('categories', 'name_')
    op.drop_column('categories', 'category')
    # ### end Alembic commands ###
