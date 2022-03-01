"""empty message

Revision ID: 5f671c4662c4
Revises: 
Create Date: 2022-03-01 11:39:23.827424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f671c4662c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sub',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stu',
    sa.Column('stu_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('snum', sa.Integer(), nullable=True),
    sa.Column('sub_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sub_id'], ['sub.id'], ),
    sa.PrimaryKeyConstraint('stu_id'),
    sa.UniqueConstraint('snum')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stu')
    op.drop_table('sub')
    # ### end Alembic commands ###
