import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WallContainerComponent } from './wall-container.component';

describe('WallContainerComponent', () => {
  let component: WallContainerComponent;
  let fixture: ComponentFixture<WallContainerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WallContainerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WallContainerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
