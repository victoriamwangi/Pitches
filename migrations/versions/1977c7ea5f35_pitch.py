"""pitch

Revision ID: 1977c7ea5f35
Revises: 378c007b1642
Create Date: 2022-05-10 13:16:17.875773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1977c7ea5f35'
down_revision = '378c007b1642'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
