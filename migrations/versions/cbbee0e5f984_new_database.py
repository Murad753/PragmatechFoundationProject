"""New Database

Revision ID: cbbee0e5f984
Revises: 
Create Date: 2021-04-01 16:48:40.966936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbbee0e5f984'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('works',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('w_title', sa.String(length=255), nullable=True),
    sa.Column('w_url', sa.String(length=255), nullable=True),
    sa.Column('w_img', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('works')
    # ### end Alembic commands ###
