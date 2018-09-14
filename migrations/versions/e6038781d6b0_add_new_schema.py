"""add new schema

Revision ID: e6038781d6b0
Revises: b11b3b277626
Create Date: 2018-09-11 23:29:01.708423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6038781d6b0'
down_revision = 'b11b3b277626'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('Category_id', sa.Integer(), nullable=True))
    op.drop_constraint('pitches_category_id_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'categories', ['Category_id'], ['id'])
    op.drop_column('pitches', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_category_id_fkey', 'pitches', 'categories', ['category_id'], ['id'])
    op.drop_column('pitches', 'Category_id')
    # ### end Alembic commands ###