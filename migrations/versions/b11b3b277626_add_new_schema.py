"""add new schema

Revision ID: b11b3b277626
Revises: 1f43c05a22a4
Create Date: 2018-09-11 21:58:03.793168

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b11b3b277626'
down_revision = '1f43c05a22a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitch')
    op.add_column('categories', sa.Column('name', sa.String(length=255), nullable=True))
    op.drop_column('categories', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('categories', 'name')
    op.create_table('pitch',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('body', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('upvotes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('downvotes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='pitch_category_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='pitch_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pitch_pkey')
    )
    op.drop_table('comments')
    op.drop_table('pitches')
    # ### end Alembic commands ###