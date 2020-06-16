"""empty message

Revision ID: fedb2cac0364
Revises: 
Create Date: 2020-03-28 18:47:32.472501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fedb2cac0364'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clothes',
    sa.Column('Cid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Uid', sa.Integer(), nullable=True),
    sa.Column('Cpic', sa.String(length=255, collation='utf8_general_ci'), nullable=True),
    sa.Column('Cname', sa.String(length=255, collation='utf8_general_ci'), nullable=True),
    sa.Column('Cclass', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Cid')
    )
    op.create_table('user',
    sa.Column('Uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Openid', sa.String(length=255, collation='utf8_general_ci'), nullable=True),
    sa.PrimaryKeyConstraint('Uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('clothes')
    # ### end Alembic commands ###
